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


class StarGifts(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.payments.StarGifts`.

    Details:
        - Layer: ``229``
        - ID: ``2ED82995``

    Parameters:
        hash (``int`` ``32-bit``):
            N/A

        gifts (List of :obj:`StarGift <stdgram.raw.base.StarGift>`):
            N/A

        chats (List of :obj:`Chat <stdgram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <stdgram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarGifts
    """

    __slots__: list[str] = ["hash", "gifts", "chats", "users"]

    ID = 0x2ed82995
    QUALNAME = "types.payments.StarGifts"

    def __init__(self, *, hash: int, gifts: list[raw.base.StarGift], chats: list[raw.base.Chat], users: list[raw.base.User]) -> None:
        self.hash = hash  # int
        self.gifts = gifts  # Vector<StarGift>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> StarGifts:
        # No flags
        
        hash = Int.read(b)
        
        gifts = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return StarGifts(hash=hash, gifts=gifts, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.hash))
        
        b.write(Vector(self.gifts))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
