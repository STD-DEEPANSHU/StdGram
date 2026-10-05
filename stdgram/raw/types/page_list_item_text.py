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


class PageListItemText(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.PageListItem`.

    Details:
        - Layer: ``229``
        - ID: ``2F58683C``

    Parameters:
        text (:obj:`RichText <stdgram.raw.base.RichText>`):
            N/A

        checkbox (``bool``, *optional*):
            N/A

        checked (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["text", "checkbox", "checked"]

    ID = 0x2f58683c
    QUALNAME = "types.PageListItemText"

    def __init__(self, *, text: raw.base.RichText, checkbox: bool | None = None, checked: bool | None = None) -> None:
        self.text = text  # RichText
        self.checkbox = checkbox  # flags.0?true
        self.checked = checked  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> PageListItemText:
        
        flags = Int.read(b)
        
        checkbox = True if flags & (1 << 0) else False
        checked = True if flags & (1 << 1) else False
        text = TLObject.read(b)
        
        return PageListItemText(text=text, checkbox=checkbox, checked=checked)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.checkbox else 0
        flags |= (1 << 1) if self.checked else 0
        b.write(Int(flags))
        
        b.write(self.text.write())
        
        return b.getvalue()
