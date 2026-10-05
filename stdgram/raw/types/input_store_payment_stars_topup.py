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


class InputStorePaymentStarsTopup(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputStorePaymentPurpose`.

    Details:
        - Layer: ``229``
        - ID: ``F9A2A6CB``

    Parameters:
        stars (``int`` ``64-bit``):
            N/A

        currency (``str``):
            N/A

        amount (``int`` ``64-bit``):
            N/A

        spend_purpose_peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["stars", "currency", "amount", "spend_purpose_peer"]

    ID = 0xf9a2a6cb
    QUALNAME = "types.InputStorePaymentStarsTopup"

    def __init__(self, *, stars: int, currency: str, amount: int, spend_purpose_peer: raw.base.InputPeer | None = None) -> None:
        self.stars = stars  # long
        self.currency = currency  # string
        self.amount = amount  # long
        self.spend_purpose_peer = spend_purpose_peer  # flags.0?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputStorePaymentStarsTopup:
        
        flags = Int.read(b)
        
        stars = Long.read(b)
        
        currency = String.read(b)
        
        amount = Long.read(b)
        
        spend_purpose_peer = TLObject.read(b) if flags & (1 << 0) else None
        
        return InputStorePaymentStarsTopup(stars=stars, currency=currency, amount=amount, spend_purpose_peer=spend_purpose_peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.spend_purpose_peer is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.stars))
        
        b.write(String(self.currency))
        
        b.write(Long(self.amount))
        
        if self.spend_purpose_peer is not None:
            b.write(self.spend_purpose_peer.write())
        
        return b.getvalue()
