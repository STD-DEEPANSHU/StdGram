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


class PeerLinkRequests(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.communities.PeerLinkRequests`.

    Details:
        - Layer: ``229``
        - ID: ``2244AFAD``

    Parameters:
        total_count (``int`` ``32-bit``):
            N/A

        requests (List of :obj:`CommunityPeerRequest <stdgram.raw.base.CommunityPeerRequest>`):
            N/A

        chats (List of :obj:`Chat <stdgram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <stdgram.raw.base.User>`):
            N/A

        next_offset (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            communities.GetPeerLinkRequests
    """

    __slots__: list[str] = ["total_count", "requests", "chats", "users", "next_offset"]

    ID = 0x2244afad
    QUALNAME = "types.communities.PeerLinkRequests"

    def __init__(self, *, total_count: int, requests: list[raw.base.CommunityPeerRequest], chats: list[raw.base.Chat], users: list[raw.base.User], next_offset: str | None = None) -> None:
        self.total_count = total_count  # int
        self.requests = requests  # Vector<CommunityPeerRequest>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.next_offset = next_offset  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> PeerLinkRequests:
        
        flags = Int.read(b)
        
        total_count = Int.read(b)
        
        requests = TLObject.read(b)
        
        next_offset = String.read(b) if flags & (1 << 0) else None
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return PeerLinkRequests(total_count=total_count, requests=requests, chats=chats, users=users, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.total_count))
        
        b.write(Vector(self.requests))
        
        if self.next_offset is not None:
            b.write(String(self.next_offset))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
