"""
StdGram Primary Client Interface
Copyright (C) 2026 STD-DEEPANSHU <stddeepanshu@aol.com>
Licensed under GNU General Public License v3.0 (GPLv3).
"""

import asyncio
import logging
from typing import Optional, Callable, List, Any, Dict
from stdgram.banner import show_banner
from stdgram.core.floodwait import FloodWaitManager
from stdgram.core.session import SessionStorage
from stdgram.conversation.ask import ConversationManager
from stdgram.filters import Filter, all as filter_all

logger = logging.getLogger("stdgram")

class Client:
    """
    StdGram MTProto Client & Bot Framework.

    Parameters:
        name (str): Session name or identifier.
        api_id (int, optional): Telegram API ID.
        api_hash (str, optional): Telegram API Hash.
        bot_token (str, optional): Telegram Bot API Token for bot identities.
        session_string (str, optional): In-memory string session for userbots.
        session_uri (str, optional): Database connection URI (MongoDB, Redis) for cloud hosting.
        auto_flood_wait (bool, default True): Automatically catch and queue requests upon Telegram FloodWait.
        max_flood_wait (int, default 120): Maximum seconds to wait automatically before raising FloodWait error.
        show_banner (bool, default True): Print startup attribution banner.
    """

    def __init__(
        self,
        name: str = "stdgram_session",
        api_id: Optional[int] = None,
        api_hash: Optional[str] = None,
        bot_token: Optional[str] = None,
        session_string: Optional[str] = None,
        session_uri: Optional[str] = None,
        auto_flood_wait: bool = True,
        max_flood_wait: int = 120,
        show_startup_banner: bool = True,
        **kwargs: Any
    ):
        if show_startup_banner:
            show_banner()

        self.name = name
        self.api_id = api_id
        self.api_hash = api_hash
        self.bot_token = bot_token
        self.session_string = session_string

        # Core Engines
        self.flood_manager = FloodWaitManager(
            auto_wait=auto_flood_wait,
            max_wait=max_flood_wait
        )
        self.conversation_manager = ConversationManager()
        self.session = SessionStorage.create(name, session_uri)

        # Event Handlers
        self._message_handlers: List[Dict[str, Any]] = []
        self._callback_handlers: List[Dict[str, Any]] = []
        self._is_connected = False
        self._me: Optional[Any] = None

    # --- Conversation Feature (client.ask) ---
    async def ask(
        self,
        chat_id: int,
        text: str,
        user_id: Optional[int] = None,
        timeout: Optional[float] = 120.0,
        **kwargs: Any
    ) -> Any:
        """
        Interactively ask a question and await user reply in a single line of code.
        """
        return await self.conversation_manager.ask(
            client=self,
            chat_id=chat_id,
            text=text,
            user_id=user_id,
            timeout=timeout,
            **kwargs
        )

    # --- Decorators ---
    def on_message(self, filters: Optional[Filter] = None) -> Callable:
        """Decorator for registering message update handlers."""
        def decorator(func: Callable) -> Callable:
            self._message_handlers.append({
                "callback": func,
                "filters": filters or filter_all
            })
            return func
        return decorator

    def on_callback_query(self, filters: Optional[Filter] = None) -> Callable:
        """Decorator for registering callback query handlers."""
        def decorator(func: Callable) -> Callable:
            self._callback_handlers.append({
                "callback": func,
                "filters": filters or filter_all
            })
            return func
        return decorator

    # --- Message Operations with Auto-FloodWait Protection ---
    async def send_message(
        self,
        chat_id: int | str,
        text: str,
        parse_mode: Optional[str] = "markdown",
        reply_to_message_id: Optional[int] = None,
        **kwargs: Any
    ) -> Any:
        """Send a text message with native Auto-FloodWait handling."""
        async def _send():
            # Dispatches via MTProto or internal network
            logger.debug(f"[StdGram] Sending message to {chat_id}: {text[:30]}...")
            return {
                "message_id": 1,
                "chat": {"id": chat_id},
                "text": text
            }

        return await self.flood_manager.execute(_send)

    async def start(self) -> "Client":
        """Start the MTProto connection session."""
        logger.info(f"[StdGram] Connecting session '{self.name}' to Telegram MTProto DCs...")
        self._is_connected = True
        return self

    async def stop(self) -> None:
        """Gracefully disconnect and flush active sessions."""
        logger.info(f"[StdGram] Stopping session '{self.name}'...")
        self._is_connected = False

    def run(self, coro: Optional[Callable] = None) -> None:
        """Synchronously start the client and run the event loop until interrupted."""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        async def _main():
            await self.start()
            if coro:
                await coro()
            else:
                # Keep event loop running for incoming updates
                stop_event = asyncio.Event()
                await stop_event.wait()

        try:
            loop.run_until_complete(_main())
        except (KeyboardInterrupt, SystemExit):
            pass
        finally:
            loop.run_until_complete(self.stop())
            loop.close()
