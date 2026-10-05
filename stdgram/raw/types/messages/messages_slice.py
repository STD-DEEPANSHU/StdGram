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


class MessagesSlice(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.messages.Messages`.

    Details:
        - Layer: ``229``
        - ID: ``5F206716``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        messages (List of :obj:`Message <stdgram.raw.base.Message>`):
            N/A

        topics (List of :obj:`ForumTopic <stdgram.raw.base.ForumTopic>`):
            N/A

        chats (List of :obj:`Chat <stdgram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <stdgram.raw.base.User>`):
            N/A

        inexact (``bool``, *optional*):
            N/A

        next_rate (``int`` ``32-bit``, *optional*):
            N/A

        offset_id_offset (``int`` ``32-bit``, *optional*):
            N/A

        search_flood (:obj:`SearchPostsFlood <stdgram.raw.base.SearchPostsFlood>`, *optional*):
            N/A

    Functions:
        This object can be returned by 18 functions.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetMessages
            messages.GetHistory
            messages.Search
            messages.SearchGlobal
            messages.GetUnreadMentions
            messages.GetRecentLocations
            messages.GetScheduledHistory
            messages.GetScheduledMessages
            messages.GetReplies
            messages.GetUnreadReactions
            messages.SearchSentMedia
            messages.GetSavedHistory
            messages.GetQuickReplyMessages
            messages.GetUnreadPollVotes
            messages.GetPersonalChannelHistory
            messages.GetRichMessage
            channels.GetMessages
            channels.SearchPosts
    """

    __slots__: list[str] = ["count", "messages", "topics", "chats", "users", "inexact", "next_rate", "offset_id_offset", "search_flood"]

    ID = 0x5f206716
    QUALNAME = "types.messages.MessagesSlice"

    def __init__(self, *, count: int, messages: list[raw.base.Message], topics: list[raw.base.ForumTopic], chats: list[raw.base.Chat], users: list[raw.base.User], inexact: bool | None = None, next_rate: int | None = None, offset_id_offset: int | None = None, search_flood: raw.base.SearchPostsFlood | None = None) -> None:
        self.count = count  # int
        self.messages = messages  # Vector<Message>
        self.topics = topics  # Vector<ForumTopic>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.inexact = inexact  # flags.1?true
        self.next_rate = next_rate  # flags.0?int
        self.offset_id_offset = offset_id_offset  # flags.2?int
        self.search_flood = search_flood  # flags.3?SearchPostsFlood

    @staticmethod
    def read(b: BytesIO, *args: Any) -> MessagesSlice:
        
        flags = Int.read(b)
        
        inexact = True if flags & (1 << 1) else False
        count = Int.read(b)
        
        next_rate = Int.read(b) if flags & (1 << 0) else None
        offset_id_offset = Int.read(b) if flags & (1 << 2) else None
        search_flood = TLObject.read(b) if flags & (1 << 3) else None
        
        messages = TLObject.read(b)
        
        topics = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return MessagesSlice(count=count, messages=messages, topics=topics, chats=chats, users=users, inexact=inexact, next_rate=next_rate, offset_id_offset=offset_id_offset, search_flood=search_flood)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.inexact else 0
        flags |= (1 << 0) if self.next_rate is not None else 0
        flags |= (1 << 2) if self.offset_id_offset is not None else 0
        flags |= (1 << 3) if self.search_flood is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        if self.next_rate is not None:
            b.write(Int(self.next_rate))
        
        if self.offset_id_offset is not None:
            b.write(Int(self.offset_id_offset))
        
        if self.search_flood is not None:
            b.write(self.search_flood.write())
        
        b.write(Vector(self.messages))
        
        b.write(Vector(self.topics))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
