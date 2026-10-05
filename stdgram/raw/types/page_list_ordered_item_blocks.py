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


class PageListOrderedItemBlocks(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.PageListOrderedItem`.

    Details:
        - Layer: ``229``
        - ID: ``8FF2D5F0``

    Parameters:
        blocks (List of :obj:`PageBlock <stdgram.raw.base.PageBlock>`):
            N/A

        checkbox (``bool``, *optional*):
            N/A

        checked (``bool``, *optional*):
            N/A

        num (``str``, *optional*):
            N/A

        value (``int`` ``32-bit``, *optional*):
            N/A

        type (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["blocks", "checkbox", "checked", "num", "value", "type"]

    ID = 0x8ff2d5f0
    QUALNAME = "types.PageListOrderedItemBlocks"

    def __init__(self, *, blocks: list[raw.base.PageBlock], checkbox: bool | None = None, checked: bool | None = None, num: str | None = None, value: int | None = None, type: str | None = None) -> None:
        self.blocks = blocks  # Vector<PageBlock>
        self.checkbox = checkbox  # flags.0?true
        self.checked = checked  # flags.1?true
        self.num = num  # flags.2?string
        self.value = value  # flags.3?int
        self.type = type  # flags.4?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> PageListOrderedItemBlocks:
        
        flags = Int.read(b)
        
        checkbox = True if flags & (1 << 0) else False
        checked = True if flags & (1 << 1) else False
        num = String.read(b) if flags & (1 << 2) else None
        blocks = TLObject.read(b)
        
        value = Int.read(b) if flags & (1 << 3) else None
        type = String.read(b) if flags & (1 << 4) else None
        return PageListOrderedItemBlocks(blocks=blocks, checkbox=checkbox, checked=checked, num=num, value=value, type=type)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.checkbox else 0
        flags |= (1 << 1) if self.checked else 0
        flags |= (1 << 2) if self.num is not None else 0
        flags |= (1 << 3) if self.value is not None else 0
        flags |= (1 << 4) if self.type is not None else 0
        b.write(Int(flags))
        
        if self.num is not None:
            b.write(String(self.num))
        
        b.write(Vector(self.blocks))
        
        if self.value is not None:
            b.write(Int(self.value))
        
        if self.type is not None:
            b.write(String(self.type))
        
        return b.getvalue()
