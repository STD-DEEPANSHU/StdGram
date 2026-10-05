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


class StickerPack(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.StickerPack`.

    Details:
        - Layer: ``229``
        - ID: ``12B299D4``

    Parameters:
        emoticon (``str``):
            N/A

        documents (List of ``int`` ``64-bit``):
            N/A

    """

    __slots__: list[str] = ["emoticon", "documents"]

    ID = 0x12b299d4
    QUALNAME = "types.StickerPack"

    def __init__(self, *, emoticon: str, documents: list[int]) -> None:
        self.emoticon = emoticon  # string
        self.documents = documents  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> StickerPack:
        # No flags
        
        emoticon = String.read(b)
        
        documents = TLObject.read(b, Long)
        
        return StickerPack(emoticon=emoticon, documents=documents)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.emoticon))
        
        b.write(Vector(self.documents, Long))
        
        return b.getvalue()
