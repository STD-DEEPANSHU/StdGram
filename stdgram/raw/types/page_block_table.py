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


class PageBlockTable(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.PageBlock`.

    Details:
        - Layer: ``229``
        - ID: ``BF4DEA82``

    Parameters:
        title (:obj:`RichText <stdgram.raw.base.RichText>`):
            N/A

        rows (List of :obj:`PageTableRow <stdgram.raw.base.PageTableRow>`):
            N/A

        bordered (``bool``, *optional*):
            N/A

        striped (``bool``, *optional*):
            N/A

        compact (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["title", "rows", "bordered", "striped", "compact"]

    ID = 0xbf4dea82
    QUALNAME = "types.PageBlockTable"

    def __init__(self, *, title: raw.base.RichText, rows: list[raw.base.PageTableRow], bordered: bool | None = None, striped: bool | None = None, compact: bool | None = None) -> None:
        self.title = title  # RichText
        self.rows = rows  # Vector<PageTableRow>
        self.bordered = bordered  # flags.0?true
        self.striped = striped  # flags.1?true
        self.compact = compact  # flags.2?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> PageBlockTable:
        
        flags = Int.read(b)
        
        bordered = True if flags & (1 << 0) else False
        striped = True if flags & (1 << 1) else False
        compact = True if flags & (1 << 2) else False
        title = TLObject.read(b)
        
        rows = TLObject.read(b)
        
        return PageBlockTable(title=title, rows=rows, bordered=bordered, striped=striped, compact=compact)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.bordered else 0
        flags |= (1 << 1) if self.striped else 0
        flags |= (1 << 2) if self.compact else 0
        b.write(Int(flags))
        
        b.write(self.title.write())
        
        b.write(Vector(self.rows))
        
        return b.getvalue()
