"""
StdGram — The Next-Generation MTProto Framework for Python
Copyright (C) 2026 STD-DEEPANSHU <stddeepanshu@aol.com>
Licensed under GNU General Public License v3.0 (GPLv3).
"""

__version__ = "1.0.0.dev1"
__author__ = "STD-DEEPANSHU"
__email__ = "stddeepanshu@aol.com"
__license__ = "GPL-3.0-only"
__copyright__ = "Copyright (C) 2026 STD-DEEPANSHU"

from .client import Client
from .banner import show_banner
from . import filters
from . import errors

__all__ = [
    "Client",
    "filters",
    "errors",
    "show_banner",
    "__version__",
    "__author__",
    "__license__",
]
