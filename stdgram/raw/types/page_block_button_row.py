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


class PageBlockButtonRow(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.PageBlock`.

    Details:
        - Layer: ``229``
        - ID: ``6D640318``

    Parameters:
        buttons (List of :obj:`PageButton <stdgram.raw.base.PageButton>`):
            N/A

        align_left (``bool``, *optional*):
            N/A

        align_center (``bool``, *optional*):
            N/A

        align_right (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["buttons", "align_left", "align_center", "align_right"]

    ID = 0x6d640318
    QUALNAME = "types.PageBlockButtonRow"

    def __init__(self, *, buttons: list[raw.base.PageButton], align_left: bool | None = None, align_center: bool | None = None, align_right: bool | None = None) -> None:
        self.buttons = buttons  # Vector<PageButton>
        self.align_left = align_left  # flags.0?true
        self.align_center = align_center  # flags.1?true
        self.align_right = align_right  # flags.2?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> PageBlockButtonRow:
        
        flags = Int.read(b)
        
        align_left = True if flags & (1 << 0) else False
        align_center = True if flags & (1 << 1) else False
        align_right = True if flags & (1 << 2) else False
        buttons = TLObject.read(b)
        
        return PageBlockButtonRow(buttons=buttons, align_left=align_left, align_center=align_center, align_right=align_right)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.align_left else 0
        flags |= (1 << 1) if self.align_center else 0
        flags |= (1 << 2) if self.align_right else 0
        b.write(Int(flags))
        
        b.write(Vector(self.buttons))
        
        return b.getvalue()
