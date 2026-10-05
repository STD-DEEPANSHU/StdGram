"""
StdGram Errors Package
"""

from .exceptions import (
    StdGramError,
    RPCError,
    FloodWait,
    ConversationTimeout,
    SessionError,
)

__all__ = [
    "StdGramError",
    "RPCError",
    "FloodWait",
    "ConversationTimeout",
    "SessionError",
]
