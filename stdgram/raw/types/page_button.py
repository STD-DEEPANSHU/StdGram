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


class PageButton(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.PageButton`.

    Details:
        - Layer: ``229``
        - ID: ``692A5488``

    Parameters:
        text (:obj:`RichText <stdgram.raw.base.RichText>`):
            N/A

        type (:obj:`InlineButtonType <stdgram.raw.base.InlineButtonType>`):
            N/A

        style (:obj:`RichButtonStyle <stdgram.raw.base.RichButtonStyle>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["text", "type", "style"]

    ID = 0x692a5488
    QUALNAME = "types.PageButton"

    def __init__(self, *, text: raw.base.RichText, type: raw.base.InlineButtonType, style: raw.base.RichButtonStyle | None = None) -> None:
        self.text = text  # RichText
        self.type = type  # InlineButtonType
        self.style = style  # flags.0?RichButtonStyle

    @staticmethod
    def read(b: BytesIO, *args: Any) -> PageButton:
        
        flags = Int.read(b)
        
        text = TLObject.read(b)
        
        type = TLObject.read(b)
        
        style = TLObject.read(b) if flags & (1 << 0) else None
        
        return PageButton(text=text, type=type, style=style)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.style is not None else 0
        b.write(Int(flags))
        
        b.write(self.text.write())
        
        b.write(self.type.write())
        
        if self.style is not None:
            b.write(self.style.write())
        
        return b.getvalue()
