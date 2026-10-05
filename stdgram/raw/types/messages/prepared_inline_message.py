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


class PreparedInlineMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.messages.PreparedInlineMessage`.

    Details:
        - Layer: ``229``
        - ID: ``FF57708D``

    Parameters:
        query_id (``int`` ``64-bit``):
            N/A

        result (:obj:`BotInlineResult <stdgram.raw.base.BotInlineResult>`):
            N/A

        peer_types (List of :obj:`InlineQueryPeerType <stdgram.raw.base.InlineQueryPeerType>`):
            N/A

        cache_time (``int`` ``32-bit``):
            N/A

        users (List of :obj:`User <stdgram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetPreparedInlineMessage
    """

    __slots__: list[str] = ["query_id", "result", "peer_types", "cache_time", "users"]

    ID = 0xff57708d
    QUALNAME = "types.messages.PreparedInlineMessage"

    def __init__(self, *, query_id: int, result: raw.base.BotInlineResult, peer_types: list[raw.base.InlineQueryPeerType], cache_time: int, users: list[raw.base.User]) -> None:
        self.query_id = query_id  # long
        self.result = result  # BotInlineResult
        self.peer_types = peer_types  # Vector<InlineQueryPeerType>
        self.cache_time = cache_time  # int
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> PreparedInlineMessage:
        # No flags
        
        query_id = Long.read(b)
        
        result = TLObject.read(b)
        
        peer_types = TLObject.read(b)
        
        cache_time = Int.read(b)
        
        users = TLObject.read(b)
        
        return PreparedInlineMessage(query_id=query_id, result=result, peer_types=peer_types, cache_time=cache_time, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.query_id))
        
        b.write(self.result.write())
        
        b.write(Vector(self.peer_types))
        
        b.write(Int(self.cache_time))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
