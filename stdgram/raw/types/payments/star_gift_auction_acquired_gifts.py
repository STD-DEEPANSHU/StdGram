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


class StarGiftAuctionAcquiredGifts(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.payments.StarGiftAuctionAcquiredGifts`.

    Details:
        - Layer: ``229``
        - ID: ``7D5BD1F0``

    Parameters:
        gifts (List of :obj:`StarGiftAuctionAcquiredGift <stdgram.raw.base.StarGiftAuctionAcquiredGift>`):
            N/A

        users (List of :obj:`User <stdgram.raw.base.User>`):
            N/A

        chats (List of :obj:`Chat <stdgram.raw.base.Chat>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarGiftAuctionAcquiredGifts
    """

    __slots__: list[str] = ["gifts", "users", "chats"]

    ID = 0x7d5bd1f0
    QUALNAME = "types.payments.StarGiftAuctionAcquiredGifts"

    def __init__(self, *, gifts: list[raw.base.StarGiftAuctionAcquiredGift], users: list[raw.base.User], chats: list[raw.base.Chat]) -> None:
        self.gifts = gifts  # Vector<StarGiftAuctionAcquiredGift>
        self.users = users  # Vector<User>
        self.chats = chats  # Vector<Chat>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> StarGiftAuctionAcquiredGifts:
        # No flags
        
        gifts = TLObject.read(b)
        
        users = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        return StarGiftAuctionAcquiredGifts(gifts=gifts, users=users, chats=chats)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.gifts))
        
        b.write(Vector(self.users))
        
        b.write(Vector(self.chats))
        
        return b.getvalue()
