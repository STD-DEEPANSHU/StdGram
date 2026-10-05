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


class KeyboardButton(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``229``
        - ID: ``2F67A72F``

    Parameters:
        text (``str``):
            N/A

        type (:obj:`ButtonType <stdgram.raw.base.ButtonType>`):
            N/A

        style (:obj:`KeyboardButtonStyle <stdgram.raw.base.KeyboardButtonStyle>`, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetRequestedWebViewButton
    """

    __slots__: list[str] = ["text", "type", "style"]

    ID = 0x2f67a72f
    QUALNAME = "types.KeyboardButton"

    def __init__(self, *, text: str, type: raw.base.ButtonType, style: raw.base.KeyboardButtonStyle | None = None) -> None:
        self.text = text  # string
        self.type = type  # ButtonType
        self.style = style  # flags.10?KeyboardButtonStyle

    @staticmethod
    def read(b: BytesIO, *args: Any) -> KeyboardButton:
        
        flags = Int.read(b)
        
        style = TLObject.read(b) if flags & (1 << 10) else None
        
        text = String.read(b)
        
        type = TLObject.read(b)
        
        return KeyboardButton(text=text, type=type, style=style)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 10) if self.style is not None else 0
        b.write(Int(flags))
        
        if self.style is not None:
            b.write(self.style.write())
        
        b.write(String(self.text))
        
        b.write(self.type.write())
        
        return b.getvalue()
