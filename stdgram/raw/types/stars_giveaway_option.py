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


class StarsGiveawayOption(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.StarsGiveawayOption`.

    Details:
        - Layer: ``229``
        - ID: ``94CE852A``

    Parameters:
        stars (``int`` ``64-bit``):
            N/A

        yearly_boosts (``int`` ``32-bit``):
            N/A

        currency (``str``):
            N/A

        amount (``int`` ``64-bit``):
            N/A

        winners (List of :obj:`StarsGiveawayWinnersOption <stdgram.raw.base.StarsGiveawayWinnersOption>`):
            N/A

        extended (``bool``, *optional*):
            N/A

        default (``bool``, *optional*):
            N/A

        store_product (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarsGiveawayOptions
    """

    __slots__: list[str] = ["stars", "yearly_boosts", "currency", "amount", "winners", "extended", "default", "store_product"]

    ID = 0x94ce852a
    QUALNAME = "types.StarsGiveawayOption"

    def __init__(self, *, stars: int, yearly_boosts: int, currency: str, amount: int, winners: list[raw.base.StarsGiveawayWinnersOption], extended: bool | None = None, default: bool | None = None, store_product: str | None = None) -> None:
        self.stars = stars  # long
        self.yearly_boosts = yearly_boosts  # int
        self.currency = currency  # string
        self.amount = amount  # long
        self.winners = winners  # Vector<StarsGiveawayWinnersOption>
        self.extended = extended  # flags.0?true
        self.default = default  # flags.1?true
        self.store_product = store_product  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> StarsGiveawayOption:
        
        flags = Int.read(b)
        
        extended = True if flags & (1 << 0) else False
        default = True if flags & (1 << 1) else False
        stars = Long.read(b)
        
        yearly_boosts = Int.read(b)
        
        store_product = String.read(b) if flags & (1 << 2) else None
        currency = String.read(b)
        
        amount = Long.read(b)
        
        winners = TLObject.read(b)
        
        return StarsGiveawayOption(stars=stars, yearly_boosts=yearly_boosts, currency=currency, amount=amount, winners=winners, extended=extended, default=default, store_product=store_product)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.extended else 0
        flags |= (1 << 1) if self.default else 0
        flags |= (1 << 2) if self.store_product is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.stars))
        
        b.write(Int(self.yearly_boosts))
        
        if self.store_product is not None:
            b.write(String(self.store_product))
        
        b.write(String(self.currency))
        
        b.write(Long(self.amount))
        
        b.write(Vector(self.winners))
        
        return b.getvalue()
