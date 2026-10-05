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


class FoundStickersNotModified(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.messages.FoundStickers`.

    Details:
        - Layer: ``229``
        - ID: ``6010C534``

    Parameters:
        next_offset (``int`` ``32-bit``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.SearchStickers
    """

    __slots__: list[str] = ["next_offset"]

    ID = 0x6010c534
    QUALNAME = "types.messages.FoundStickersNotModified"

    def __init__(self, *, next_offset: int | None = None) -> None:
        self.next_offset = next_offset  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> FoundStickersNotModified:
        
        flags = Int.read(b)
        
        next_offset = Int.read(b) if flags & (1 << 0) else None
        return FoundStickersNotModified(next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        b.write(Int(flags))
        
        if self.next_offset is not None:
            b.write(Int(self.next_offset))
        
        return b.getvalue()
