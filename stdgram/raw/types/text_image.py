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


class TextImage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.RichText`.

    Details:
        - Layer: ``229``
        - ID: ``81CCF4F``

    Parameters:
        document_id (``int`` ``64-bit``):
            N/A

        w (``int`` ``32-bit``):
            N/A

        h (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["document_id", "w", "h"]

    ID = 0x81ccf4f
    QUALNAME = "types.TextImage"

    def __init__(self, *, document_id: int, w: int, h: int) -> None:
        self.document_id = document_id  # long
        self.w = w  # int
        self.h = h  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> TextImage:
        # No flags
        
        document_id = Long.read(b)
        
        w = Int.read(b)
        
        h = Int.read(b)
        
        return TextImage(document_id=document_id, w=w, h=h)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.document_id))
        
        b.write(Int(self.w))
        
        b.write(Int(self.h))
        
        return b.getvalue()
