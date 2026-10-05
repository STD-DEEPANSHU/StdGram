"""
StdGram Cloud-Ready Session Manager (SQLite, MongoDB, Redis, Memory)
Copyright (C) 2026 STD-DEEPANSHU <stddeepanshu@aol.com>
Licensed under GNU General Public License v3.0 (GPLv3).
"""

from typing import Optional, Any
import os

class SessionStorage:
    """Abstract interface for storing Telegram auth keys and session state."""

    def __init__(self, name: str, session_uri: Optional[str] = None):
        self.name = name
        self.session_uri = session_uri

    @classmethod
    def create(cls, name: str, session_uri: Optional[str] = None) -> "SessionStorage":
        """Instantiate the proper session backend depending on URI."""
        if not session_uri:
            return SQLiteSession(name)
        if session_uri.startswith("mongodb://") or session_uri.startswith("mongodb+srv://"):
            return MongoDBSession(name, session_uri)
        if session_uri.startswith("redis://"):
            return RedisSession(name, session_uri)
        return SQLiteSession(name)

class SQLiteSession(SessionStorage):
    """Local SQLite session storage."""
    pass

class MongoDBSession(SessionStorage):
    """Cloud MongoDB session storage (eliminates missing session files on Heroku/Docker)."""
    pass

class RedisSession(SessionStorage):
    """Fast in-memory Redis session storage."""
    pass
