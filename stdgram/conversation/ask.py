"""
StdGram Native Conversation & Interactive Prompt Engine (`client.ask`)
Copyright (C) 2026 STD-DEEPANSHU <stddeepanshu@aol.com>
Licensed under GNU General Public License v3.0 (GPLv3).
"""

import asyncio
from typing import Dict, Tuple, Optional, Any, Callable
from stdgram.errors import ConversationTimeout

class ConversationManager:
    """
    Handles step-by-step interactive user conversations and questions natively.
    Enables `await client.ask(chat_id, "Enter your name:")` without external plugins.
    """

    def __init__(self):
        # Maps (chat_id, user_id) -> asyncio.Future
        self._listeners: Dict[Tuple[int, Optional[int]], asyncio.Future] = {}

    def register_listener(
        self,
        chat_id: int,
        user_id: Optional[int] = None
    ) -> asyncio.Future:
        """Register a pending expectation for the user's next message."""
        loop = asyncio.get_running_loop()
        future = loop.create_future()
        self._listeners[(chat_id, user_id)] = future
        return future

    def unregister_listener(
        self,
        chat_id: int,
        user_id: Optional[int] = None
    ) -> None:
        """Unregister a listener once resolved or cancelled."""
        self._listeners.pop((chat_id, user_id), None)

    def handle_incoming_message(self, message: Any) -> bool:
        """
        Check if an incoming message satisfies any pending conversation listener.
        Returns True if the message was captured by an active conversation.
        """
        chat_id = getattr(getattr(message, "chat", None), "id", None)
        user_id = getattr(getattr(message, "from_user", None), "id", None)

        if not chat_id:
            return False

        # Try specific user match first, then chat-wide match
        future = self._listeners.get((chat_id, user_id)) or self._listeners.get((chat_id, None))

        if future and not future.done():
            future.set_result(message)
            self.unregister_listener(chat_id, user_id)
            self.unregister_listener(chat_id, None)
            return True

        return False

    async def ask(
        self,
        client: Any,
        chat_id: int,
        text: str,
        user_id: Optional[int] = None,
        timeout: Optional[float] = 120.0,
        **kwargs: Any
    ) -> Any:
        """
        Sends a question and awaits the user's reply in a single asynchronous call.
        """
        # Send prompt question message
        await client.send_message(chat_id, text, **kwargs)

        # Register expectation
        future = self.register_listener(chat_id, user_id)

        try:
            if timeout:
                return await asyncio.wait_for(future, timeout=timeout)
            return await future
        except asyncio.TimeoutError:
            self.unregister_listener(chat_id, user_id)
            raise ConversationTimeout(
                f"Conversation with chat {chat_id} timed out after {timeout}s."
            )
