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


class AffectedFoundMessages(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.messages.AffectedFoundMessages`.

    Details:
        - Layer: ``229``
        - ID: ``EF8D3E6C``

    Parameters:
        pts (``int`` ``32-bit``):
            N/A

        pts_count (``int`` ``32-bit``):
            N/A

        offset (``int`` ``32-bit``):
            N/A

        messages (List of ``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.DeletePhoneCallHistory
    """

    __slots__: list[str] = ["pts", "pts_count", "offset", "messages"]

    ID = 0xef8d3e6c
    QUALNAME = "types.messages.AffectedFoundMessages"

    def __init__(self, *, pts: int, pts_count: int, offset: int, messages: list[int]) -> None:
        self.pts = pts  # int
        self.pts_count = pts_count  # int
        self.offset = offset  # int
        self.messages = messages  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> AffectedFoundMessages:
        # No flags
        
        pts = Int.read(b)
        
        pts_count = Int.read(b)
        
        offset = Int.read(b)
        
        messages = TLObject.read(b, Int)
        
        return AffectedFoundMessages(pts=pts, pts_count=pts_count, offset=offset, messages=messages)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.pts))
        
        b.write(Int(self.pts_count))
        
        b.write(Int(self.offset))
        
        b.write(Vector(self.messages, Int))
        
        return b.getvalue()
