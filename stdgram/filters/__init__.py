"""
StdGram Composable Event Filters
Copyright (C) 2026 STD-DEEPANSHU <stddeepanshu@aol.com>
Licensed under GNU General Public License v3.0 (GPLv3).
"""

from typing import Callable, Any, List, Union

class Filter:
    """Base composable message filter supporting boolean operators (&, |, ~)."""

    def __init__(self, func: Callable[[Any, Any], bool]):
        self.func = func

    async def __call__(self, client: Any, update: Any) -> bool:
        res = self.func(client, update)
        if hasattr(res, "__await__"):
            return await res
        return bool(res)

    def __invert__(self) -> "Filter":
        async def _not(client: Any, update: Any) -> bool:
            return not await self(client, update)
        return Filter(_not)

    def __and__(self, other: "Filter") -> "Filter":
        async def _and(client: Any, update: Any) -> bool:
            return (await self(client, update)) and (await other(client, update))
        return Filter(_and)

    def __or__(self, other: "Filter") -> "Filter":
        async def _or(client: Any, update: Any) -> bool:
            return (await self(client, update)) or (await other(client, update))
        return Filter(_or)

def create(func: Callable[[Any, Any], bool]) -> Filter:
    """Create a custom filter from a function."""
    return Filter(func)

# Built-in Filters
all = Filter(lambda _, __: True)
text = Filter(lambda _, m: bool(getattr(m, "text", None)))
media = Filter(lambda _, m: bool(getattr(m, "media", None)))
photo = Filter(lambda _, m: bool(getattr(m, "photo", None)))
video = Filter(lambda _, m: bool(getattr(m, "video", None)))
document = Filter(lambda _, m: bool(getattr(m, "document", None)))
private = Filter(lambda _, m: getattr(getattr(m, "chat", None), "type", "") == "private")
group = Filter(lambda _, m: getattr(getattr(m, "chat", None), "type", "") in ("group", "supergroup"))
channel = Filter(lambda _, m: getattr(getattr(m, "chat", None), "type", "") == "channel")

def command(commands: Union[str, List[str]], prefixes: str = "/") -> Filter:
    """Filter messages matching specific command triggers."""
    if isinstance(commands, str):
        commands = [commands]
    commands = [c.lower() for c in commands]

    def _command_filter(_, m: Any) -> bool:
        t = getattr(m, "text", "") or ""
        if not t or not any(t.startswith(p) for p in prefixes):
            return False
        cmd = t[1:].split()[0].lower().split("@")[0]
        return cmd in commands

    return Filter(_command_filter)
