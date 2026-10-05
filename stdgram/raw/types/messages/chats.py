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


class Chats(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.messages.Chats`.

    Details:
        - Layer: ``229``
        - ID: ``64FF9FD5``

    Parameters:
        chats (List of :obj:`Chat <stdgram.raw.base.Chat>`):
            N/A

    Functions:
        This object can be returned by 9 functions.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetChats
            messages.GetCommonChats
            channels.GetChannels
            channels.GetAdminedPublicChannels
            channels.GetLeftChannels
            channels.GetGroupsForDiscussion
            channels.GetChannelRecommendations
            stories.GetChatsToSend
            communities.GetJoinedCommunities
    """

    __slots__: list[str] = ["chats"]

    ID = 0x64ff9fd5
    QUALNAME = "types.messages.Chats"

    def __init__(self, *, chats: list[raw.base.Chat]) -> None:
        self.chats = chats  # Vector<Chat>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> Chats:
        # No flags
        
        chats = TLObject.read(b)
        
        return Chats(chats=chats)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.chats))
        
        return b.getvalue()
