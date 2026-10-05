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


class GetStarGiftAuctionState(TLObject["raw.base.payments.StarGiftAuctionState"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``5C9FF4D6``

    Parameters:
        auction (:obj:`InputStarGiftAuction <stdgram.raw.base.InputStarGiftAuction>`):
            N/A

        version (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`payments.StarGiftAuctionState <stdgram.raw.base.payments.StarGiftAuctionState>`
    """

    __slots__: list[str] = ["auction", "version"]

    ID = 0x5c9ff4d6
    QUALNAME = "functions.payments.GetStarGiftAuctionState"

    def __init__(self, *, auction: raw.base.InputStarGiftAuction, version: int) -> None:
        self.auction = auction  # InputStarGiftAuction
        self.version = version  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GetStarGiftAuctionState:
        # No flags
        
        auction = TLObject.read(b)
        
        version = Int.read(b)
        
        return GetStarGiftAuctionState(auction=auction, version=version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.auction.write())
        
        b.write(Int(self.version))
        
        return b.getvalue()
