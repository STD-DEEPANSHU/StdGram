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


class GroupParticipants(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.phone.GroupParticipants`.

    Details:
        - Layer: ``229``
        - ID: ``F47751B6``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        participants (List of :obj:`GroupCallParticipant <stdgram.raw.base.GroupCallParticipant>`):
            N/A

        next_offset (``str``):
            N/A

        chats (List of :obj:`Chat <stdgram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <stdgram.raw.base.User>`):
            N/A

        version (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            phone.GetGroupParticipants
    """

    __slots__: list[str] = ["count", "participants", "next_offset", "chats", "users", "version"]

    ID = 0xf47751b6
    QUALNAME = "types.phone.GroupParticipants"

    def __init__(self, *, count: int, participants: list[raw.base.GroupCallParticipant], next_offset: str, chats: list[raw.base.Chat], users: list[raw.base.User], version: int) -> None:
        self.count = count  # int
        self.participants = participants  # Vector<GroupCallParticipant>
        self.next_offset = next_offset  # string
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.version = version  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GroupParticipants:
        # No flags
        
        count = Int.read(b)
        
        participants = TLObject.read(b)
        
        next_offset = String.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        version = Int.read(b)
        
        return GroupParticipants(count=count, participants=participants, next_offset=next_offset, chats=chats, users=users, version=version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.count))
        
        b.write(Vector(self.participants))
        
        b.write(String(self.next_offset))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        b.write(Int(self.version))
        
        return b.getvalue()
