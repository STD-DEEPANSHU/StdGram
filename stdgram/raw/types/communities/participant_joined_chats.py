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


class ParticipantJoinedChats(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.communities.ParticipantJoinedChats`.

    Details:
        - Layer: ``229``
        - ID: ``8D78512A``

    Parameters:
        creator_chat_ids (List of ``int`` ``64-bit``):
            N/A

        joined_chat_ids (List of ``int`` ``64-bit``):
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

            communities.GetParticipantJoinedChats
    """

    __slots__: list[str] = ["creator_chat_ids", "joined_chat_ids", "chats", "users"]

    ID = 0x8d78512a
    QUALNAME = "types.communities.ParticipantJoinedChats"

    def __init__(self, *, creator_chat_ids: list[int], joined_chat_ids: list[int], chats: list[raw.base.Chat], users: list[raw.base.User]) -> None:
        self.creator_chat_ids = creator_chat_ids  # Vector<long>
        self.joined_chat_ids = joined_chat_ids  # Vector<long>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> ParticipantJoinedChats:
        # No flags
        
        creator_chat_ids = TLObject.read(b, Long)
        
        joined_chat_ids = TLObject.read(b, Long)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return ParticipantJoinedChats(creator_chat_ids=creator_chat_ids, joined_chat_ids=joined_chat_ids, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.creator_chat_ids, Long))
        
        b.write(Vector(self.joined_chat_ids, Long))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
