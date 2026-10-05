"""
StdGram Native Auto-FloodWait Manager & Queue Engine
Copyright (C) 2026 STD-DEEPANSHU <stddeepanshu@aol.com>
Licensed under GNU General Public License v3.0 (GPLv3).
"""

import asyncio
import logging
from typing import Callable, Any, Coroutine, Optional
from stdgram.errors import FloodWait

logger = logging.getLogger("stdgram.floodwait")

class FloodWaitManager:
    """
    Manages rate limits (FloodWait) automatically across all StdGram requests.
    Prevents bot crashes by safely queuing and pausing requests when Telegram rate limits occur.
    """

    def __init__(self, auto_wait: bool = True, max_wait: int = 120):
        self.auto_wait = auto_wait
        self.max_wait = max_wait
        self._lock = asyncio.Lock()
        self._is_paused = False
        self._pause_until = 0.0

    async def execute(
        self,
        func: Callable[..., Coroutine[Any, Any, Any]],
        *args: Any,
        **kwargs: Any
    ) -> Any:
        """
        Execute an asynchronous Telegram MTProto call with auto-floodwait protection.
        """
        if not self.auto_wait:
            return await func(*args, **kwargs)

        while True:
            # Check if global wait lock is active
            loop = asyncio.get_running_loop()
            current_time = loop.time()
            if self._is_paused and current_time < self._pause_until:
                wait_time = self._pause_until - current_time
                logger.warning(
                    f"[StdGram Auto-FloodWait] Global queue paused. Waiting {wait_time:.1f}s..."
                )
                await asyncio.sleep(wait_time)

            try:
                return await func(*args, **kwargs)
            except FloodWait as error:
                wait_seconds = int(error.value)
                logger.warning(
                    f"[StdGram Auto-FloodWait] Telegram rate-limit detected: {wait_seconds}s for {func.__name__}."
                )

                if wait_seconds > self.max_wait:
                    logger.error(
                        f"[StdGram Auto-FloodWait] Wait duration {wait_seconds}s exceeds max_wait ({self.max_wait}s). Raising."
                    )
                    raise error

                async with self._lock:
                    self._is_paused = True
                    self._pause_until = loop.time() + wait_seconds + 1.0

                logger.info(
                    f"[StdGram Auto-FloodWait] Sleeping for {wait_seconds + 1}s before automatic retry..."
                )
                await asyncio.sleep(wait_seconds + 1.0)
                self._is_paused = False
