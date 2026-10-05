"""
StdGram Console Banner & Legal Notices
Copyright (C) 2026 STD-DEEPANSHU <stddeepanshu@aol.com>
Licensed under GNU General Public License v3.0 (GPLv3).
"""

import sys

BANNER_TEXT = r"""
  ____  _       _  ____                     
 / ___|| |_  __| |/ ___|_ __ __ _ _ __ ___  
 \___ \| __|/ _` | |  _| '__/ _` | '_ ` _ \ 
  ___) | |_| (_| | |_| | | | (_| | | | | | |
 |____/ \__|\__,_|\____|_|  \__,_|_| |_| |_|
=====================================================
⚡ StdGram v1.0.0.dev1 — Next-Gen MTProto Framework
👤 Lead Architect: STD-DEEPANSHU
📜 License: GNU General Public License v3.0 (GPLv3)
🌐 GitHub: https://github.com/STD-DEEPANSHU/StdGram
=====================================================
"""

_BANNER_SHOWN = False

def show_banner(force: bool = False) -> None:
    """Print the official StdGram startup banner once upon client initialization."""
    global _BANNER_SHOWN
    if not _BANNER_SHOWN or force:
        try:
            sys.stdout.write(BANNER_TEXT + "\n")
            sys.stdout.flush()
        except Exception:
            pass
        _BANNER_SHOWN = True
