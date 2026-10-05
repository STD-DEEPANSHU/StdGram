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


class StarGiftAuctionRound(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.StarGiftAuctionRound`.

    Details:
        - Layer: ``229``
        - ID: ``3AAE0528``

    Parameters:
        num (``int`` ``32-bit``):
            N/A

        duration (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["num", "duration"]

    ID = 0x3aae0528
    QUALNAME = "types.StarGiftAuctionRound"

    def __init__(self, *, num: int, duration: int) -> None:
        self.num = num  # int
        self.duration = duration  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> StarGiftAuctionRound:
        # No flags
        
        num = Int.read(b)
        
        duration = Int.read(b)
        
        return StarGiftAuctionRound(num=num, duration=duration)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.num))
        
        b.write(Int(self.duration))
        
        return b.getvalue()
