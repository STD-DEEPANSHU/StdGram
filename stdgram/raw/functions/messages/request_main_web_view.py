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


class RequestMainWebView(TLObject["raw.base.WebViewResult"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``C9E01E7B``

    Parameters:
        peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        bot (:obj:`InputUser <stdgram.raw.base.InputUser>`):
            N/A

        platform (``str``):
            N/A

        compact (``bool``, *optional*):
            N/A

        fullscreen (``bool``, *optional*):
            N/A

        start_param (``str``, *optional*):
            N/A

        theme_params (:obj:`DataJSON <stdgram.raw.base.DataJSON>`, *optional*):
            N/A

    Returns:
        :obj:`WebViewResult <stdgram.raw.base.WebViewResult>`
    """

    __slots__: list[str] = ["peer", "bot", "platform", "compact", "fullscreen", "start_param", "theme_params"]

    ID = 0xc9e01e7b
    QUALNAME = "functions.messages.RequestMainWebView"

    def __init__(self, *, peer: raw.base.InputPeer, bot: raw.base.InputUser, platform: str, compact: bool | None = None, fullscreen: bool | None = None, start_param: str | None = None, theme_params: raw.base.DataJSON | None = None) -> None:
        self.peer = peer  # InputPeer
        self.bot = bot  # InputUser
        self.platform = platform  # string
        self.compact = compact  # flags.7?true
        self.fullscreen = fullscreen  # flags.8?true
        self.start_param = start_param  # flags.1?string
        self.theme_params = theme_params  # flags.0?DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> RequestMainWebView:
        
        flags = Int.read(b)
        
        compact = True if flags & (1 << 7) else False
        fullscreen = True if flags & (1 << 8) else False
        peer = TLObject.read(b)
        
        bot = TLObject.read(b)
        
        start_param = String.read(b) if flags & (1 << 1) else None
        theme_params = TLObject.read(b) if flags & (1 << 0) else None
        
        platform = String.read(b)
        
        return RequestMainWebView(peer=peer, bot=bot, platform=platform, compact=compact, fullscreen=fullscreen, start_param=start_param, theme_params=theme_params)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 7) if self.compact else 0
        flags |= (1 << 8) if self.fullscreen else 0
        flags |= (1 << 1) if self.start_param is not None else 0
        flags |= (1 << 0) if self.theme_params is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(self.bot.write())
        
        if self.start_param is not None:
            b.write(String(self.start_param))
        
        if self.theme_params is not None:
            b.write(self.theme_params.write())
        
        b.write(String(self.platform))
        
        return b.getvalue()
