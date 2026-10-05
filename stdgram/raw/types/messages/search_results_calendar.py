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


class SearchResultsCalendar(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.messages.SearchResultsCalendar`.

    Details:
        - Layer: ``229``
        - ID: ``147EE23C``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        min_date (``int`` ``32-bit``):
            N/A

        min_msg_id (``int`` ``32-bit``):
            N/A

        periods (List of :obj:`SearchResultsCalendarPeriod <stdgram.raw.base.SearchResultsCalendarPeriod>`):
            N/A

        messages (List of :obj:`Message <stdgram.raw.base.Message>`):
            N/A

        chats (List of :obj:`Chat <stdgram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <stdgram.raw.base.User>`):
            N/A

        inexact (``bool``, *optional*):
            N/A

        offset_id_offset (``int`` ``32-bit``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSearchResultsCalendar
    """

    __slots__: list[str] = ["count", "min_date", "min_msg_id", "periods", "messages", "chats", "users", "inexact", "offset_id_offset"]

    ID = 0x147ee23c
    QUALNAME = "types.messages.SearchResultsCalendar"

    def __init__(self, *, count: int, min_date: int, min_msg_id: int, periods: list[raw.base.SearchResultsCalendarPeriod], messages: list[raw.base.Message], chats: list[raw.base.Chat], users: list[raw.base.User], inexact: bool | None = None, offset_id_offset: int | None = None) -> None:
        self.count = count  # int
        self.min_date = min_date  # int
        self.min_msg_id = min_msg_id  # int
        self.periods = periods  # Vector<SearchResultsCalendarPeriod>
        self.messages = messages  # Vector<Message>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.inexact = inexact  # flags.0?true
        self.offset_id_offset = offset_id_offset  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SearchResultsCalendar:
        
        flags = Int.read(b)
        
        inexact = True if flags & (1 << 0) else False
        count = Int.read(b)
        
        min_date = Int.read(b)
        
        min_msg_id = Int.read(b)
        
        offset_id_offset = Int.read(b) if flags & (1 << 1) else None
        periods = TLObject.read(b)
        
        messages = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return SearchResultsCalendar(count=count, min_date=min_date, min_msg_id=min_msg_id, periods=periods, messages=messages, chats=chats, users=users, inexact=inexact, offset_id_offset=offset_id_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.inexact else 0
        flags |= (1 << 1) if self.offset_id_offset is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        b.write(Int(self.min_date))
        
        b.write(Int(self.min_msg_id))
        
        if self.offset_id_offset is not None:
            b.write(Int(self.offset_id_offset))
        
        b.write(Vector(self.periods))
        
        b.write(Vector(self.messages))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
