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


class RequestSimpleWebView(TLObject["raw.base.WebViewResult"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``413A3E73``

    Parameters:
        bot (:obj:`InputUser <stdgram.raw.base.InputUser>`):
            N/A

        platform (``str``):
            N/A

        from_switch_webview (``bool``, *optional*):
            N/A

        from_side_menu (``bool``, *optional*):
            N/A

        compact (``bool``, *optional*):
            N/A

        fullscreen (``bool``, *optional*):
            N/A

        url (``str``, *optional*):
            N/A

        start_param (``str``, *optional*):
            N/A

        theme_params (:obj:`DataJSON <stdgram.raw.base.DataJSON>`, *optional*):
            N/A

    Returns:
        :obj:`WebViewResult <stdgram.raw.base.WebViewResult>`
    """

    __slots__: list[str] = ["bot", "platform", "from_switch_webview", "from_side_menu", "compact", "fullscreen", "url", "start_param", "theme_params"]

    ID = 0x413a3e73
    QUALNAME = "functions.messages.RequestSimpleWebView"

    def __init__(self, *, bot: raw.base.InputUser, platform: str, from_switch_webview: bool | None = None, from_side_menu: bool | None = None, compact: bool | None = None, fullscreen: bool | None = None, url: str | None = None, start_param: str | None = None, theme_params: raw.base.DataJSON | None = None) -> None:
        self.bot = bot  # InputUser
        self.platform = platform  # string
        self.from_switch_webview = from_switch_webview  # flags.1?true
        self.from_side_menu = from_side_menu  # flags.2?true
        self.compact = compact  # flags.7?true
        self.fullscreen = fullscreen  # flags.8?true
        self.url = url  # flags.3?string
        self.start_param = start_param  # flags.4?string
        self.theme_params = theme_params  # flags.0?DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> RequestSimpleWebView:
        
        flags = Int.read(b)
        
        from_switch_webview = True if flags & (1 << 1) else False
        from_side_menu = True if flags & (1 << 2) else False
        compact = True if flags & (1 << 7) else False
        fullscreen = True if flags & (1 << 8) else False
        bot = TLObject.read(b)
        
        url = String.read(b) if flags & (1 << 3) else None
        start_param = String.read(b) if flags & (1 << 4) else None
        theme_params = TLObject.read(b) if flags & (1 << 0) else None
        
        platform = String.read(b)
        
        return RequestSimpleWebView(bot=bot, platform=platform, from_switch_webview=from_switch_webview, from_side_menu=from_side_menu, compact=compact, fullscreen=fullscreen, url=url, start_param=start_param, theme_params=theme_params)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.from_switch_webview else 0
        flags |= (1 << 2) if self.from_side_menu else 0
        flags |= (1 << 7) if self.compact else 0
        flags |= (1 << 8) if self.fullscreen else 0
        flags |= (1 << 3) if self.url is not None else 0
        flags |= (1 << 4) if self.start_param is not None else 0
        flags |= (1 << 0) if self.theme_params is not None else 0
        b.write(Int(flags))
        
        b.write(self.bot.write())
        
        if self.url is not None:
            b.write(String(self.url))
        
        if self.start_param is not None:
            b.write(String(self.start_param))
        
        if self.theme_params is not None:
            b.write(self.theme_params.write())
        
        b.write(String(self.platform))
        
        return b.getvalue()
