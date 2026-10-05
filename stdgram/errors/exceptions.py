"""
StdGram Exceptions Hierarchy
Copyright (C) 2026 STD-DEEPANSHU <stddeepanshu@aol.com>
Licensed under GNU GPLv3.
"""

class StdGramError(Exception):
    """Base exception for all StdGram related errors."""
    pass

class RPCError(StdGramError):
    """Base exception for Telegram MTProto RPC errors."""
    def __init__(self, code: int = 0, message: str = ""):
        self.code = code
        self.message = message
        super().__init__(f"[{code}] {message}" if code else message)

class FloodWait(RPCError):
    """
    Exception raised when Telegram rate-limits requests.
    Contains the required wait duration in seconds.
    """
    def __init__(self, value: int = 0):
        self.value = value
        super().__init__(420, f"A wait of {value} seconds is required (FLOOD_WAIT_{value})")

class ConversationTimeout(StdGramError):
    """Raised when an interactive client.ask() prompt times out waiting for reply."""
    pass

class SessionError(StdGramError):
    """Raised when session storage or authorization fails."""
    pass
