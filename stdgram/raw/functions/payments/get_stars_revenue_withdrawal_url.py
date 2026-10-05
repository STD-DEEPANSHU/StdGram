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


class GetStarsRevenueWithdrawalUrl(TLObject["raw.base.payments.StarsRevenueWithdrawalUrl"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``2433DC92``

    Parameters:
        peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        password (:obj:`InputCheckPasswordSRP <stdgram.raw.base.InputCheckPasswordSRP>`):
            N/A

        ton (``bool``, *optional*):
            N/A

        amount (``int`` ``64-bit``, *optional*):
            N/A

    Returns:
        :obj:`payments.StarsRevenueWithdrawalUrl <stdgram.raw.base.payments.StarsRevenueWithdrawalUrl>`
    """

    __slots__: list[str] = ["peer", "password", "ton", "amount"]

    ID = 0x2433dc92
    QUALNAME = "functions.payments.GetStarsRevenueWithdrawalUrl"

    def __init__(self, *, peer: raw.base.InputPeer, password: raw.base.InputCheckPasswordSRP, ton: bool | None = None, amount: int | None = None) -> None:
        self.peer = peer  # InputPeer
        self.password = password  # InputCheckPasswordSRP
        self.ton = ton  # flags.0?true
        self.amount = amount  # flags.1?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GetStarsRevenueWithdrawalUrl:
        
        flags = Int.read(b)
        
        ton = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        amount = Long.read(b) if flags & (1 << 1) else None
        password = TLObject.read(b)
        
        return GetStarsRevenueWithdrawalUrl(peer=peer, password=password, ton=ton, amount=amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.ton else 0
        flags |= (1 << 1) if self.amount is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.amount is not None:
            b.write(Long(self.amount))
        
        b.write(self.password.write())
        
        return b.getvalue()
