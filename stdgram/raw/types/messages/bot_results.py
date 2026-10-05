#  StdGram - Telegram MTProto API Client Library for Python
#
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#  Copyright (C) 2024-present KurimuzonAkuma <https://github.com/KurimuzonAkuma>
#
#  This file is part of StdGram.
#
#  StdGram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  StdGram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with StdGram. If not, see <https://www.gnu.org/licenses/>.

from __future__ import annotations as _annotations

from io import BytesIO
from typing import TYPE_CHECKING, Any

from stdgram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from stdgram.raw.core import TLObject

if TYPE_CHECKING:
    from stdgram import raw

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class BotResults(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.messages.BotResults`.

    Details:
        - Layer: ``229``
        - ID: ``E021F2F6``

    Parameters:
        query_id (``int`` ``64-bit``):
            N/A

        results (List of :obj:`BotInlineResult <stdgram.raw.base.BotInlineResult>`):
            N/A

        cache_time (``int`` ``32-bit``):
            N/A

        users (List of :obj:`User <stdgram.raw.base.User>`):
            N/A

        gallery (``bool``, *optional*):
            N/A

        next_offset (``str``, *optional*):
            N/A

        switch_pm (:obj:`InlineBotSwitchPM <stdgram.raw.base.InlineBotSwitchPM>`, *optional*):
            N/A

        switch_webview (:obj:`InlineBotWebView <stdgram.raw.base.InlineBotWebView>`, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetInlineBotResults
    """

    __slots__: list[str] = ["query_id", "results", "cache_time", "users", "gallery", "next_offset", "switch_pm", "switch_webview"]

    ID = 0xe021f2f6
    QUALNAME = "types.messages.BotResults"

    def __init__(self, *, query_id: int, results: list[raw.base.BotInlineResult], cache_time: int, users: list[raw.base.User], gallery: bool | None = None, next_offset: str | None = None, switch_pm: raw.base.InlineBotSwitchPM | None = None, switch_webview: raw.base.InlineBotWebView | None = None) -> None:
        self.query_id = query_id  # long
        self.results = results  # Vector<BotInlineResult>
        self.cache_time = cache_time  # int
        self.users = users  # Vector<User>
        self.gallery = gallery  # flags.0?true
        self.next_offset = next_offset  # flags.1?string
        self.switch_pm = switch_pm  # flags.2?InlineBotSwitchPM
        self.switch_webview = switch_webview  # flags.3?InlineBotWebView

    @staticmethod
    def read(b: BytesIO, *args: Any) -> BotResults:
        
        flags = Int.read(b)
        
        gallery = True if flags & (1 << 0) else False
        query_id = Long.read(b)
        
        next_offset = String.read(b) if flags & (1 << 1) else None
        switch_pm = TLObject.read(b) if flags & (1 << 2) else None
        
        switch_webview = TLObject.read(b) if flags & (1 << 3) else None
        
        results = TLObject.read(b)
        
        cache_time = Int.read(b)
        
        users = TLObject.read(b)
        
        return BotResults(query_id=query_id, results=results, cache_time=cache_time, users=users, gallery=gallery, next_offset=next_offset, switch_pm=switch_pm, switch_webview=switch_webview)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.gallery else 0
        flags |= (1 << 1) if self.next_offset is not None else 0
        flags |= (1 << 2) if self.switch_pm is not None else 0
        flags |= (1 << 3) if self.switch_webview is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.query_id))
        
        if self.next_offset is not None:
            b.write(String(self.next_offset))
        
        if self.switch_pm is not None:
            b.write(self.switch_pm.write())
        
        if self.switch_webview is not None:
            b.write(self.switch_webview.write())
        
        b.write(Vector(self.results))
        
        b.write(Int(self.cache_time))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
