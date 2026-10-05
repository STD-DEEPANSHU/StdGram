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


class GroupCallStars(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.phone.GroupCallStars`.

    Details:
        - Layer: ``229``
        - ID: ``9D1DBD26``

    Parameters:
        total_stars (``int`` ``64-bit``):
            N/A

        top_donors (List of :obj:`GroupCallDonor <stdgram.raw.base.GroupCallDonor>`):
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

            phone.GetGroupCallStars
    """

    __slots__: list[str] = ["total_stars", "top_donors", "chats", "users"]

    ID = 0x9d1dbd26
    QUALNAME = "types.phone.GroupCallStars"

    def __init__(self, *, total_stars: int, top_donors: list[raw.base.GroupCallDonor], chats: list[raw.base.Chat], users: list[raw.base.User]) -> None:
        self.total_stars = total_stars  # long
        self.top_donors = top_donors  # Vector<GroupCallDonor>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GroupCallStars:
        # No flags
        
        total_stars = Long.read(b)
        
        top_donors = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return GroupCallStars(total_stars=total_stars, top_donors=top_donors, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.total_stars))
        
        b.write(Vector(self.top_donors))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
