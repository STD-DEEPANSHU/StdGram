#  StdGram - Telegram MTProto API Client & Framework for Python
#  Copyright (C) 2026 STD-DEEPANSHU <stddeepanshu@aol.com>
#  Licensed under GNU General Public License v3.0 (GPLv3).

__version__ = "1.0.0.dev1"
__license__ = "GNU General Public License v3.0 (GPLv3)"
__copyright__ = "Copyright (C) 2026 STD-DEEPANSHU <stddeepanshu@aol.com>"
__author__ = "STD-DEEPANSHU"


class StopTransmission(Exception):
    pass


class StopPropagation(StopAsyncIteration):
    pass


class ContinuePropagation(StopAsyncIteration):
    pass


from . import enums, errors, filters, handlers, raw, types, core, conversation
from .client import Client
from .sync import compose, idle
from .banner import show_banner

__all__ = [
    "Client",
    "ContinuePropagation",
    "StopPropagation",
    "StopTransmission",
    "compose",
    "enums",
    "errors",
    "filters",
    "handlers",
    "idle",
    "raw",
    "types",
    "core",
    "conversation",
    "show_banner",
]
