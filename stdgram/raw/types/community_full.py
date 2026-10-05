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


class CommunityFull(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.ChatFull`.

    Details:
        - Layer: ``229``
        - ID: ``CBB7A507``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        about (``str``):
            N/A

        chat_photo (:obj:`Photo <stdgram.raw.base.Photo>`):
            N/A

        linked_peers (List of :obj:`CommunityPeer <stdgram.raw.base.CommunityPeer>`):
            N/A

        admins_count (``int`` ``32-bit``, *optional*):
            N/A

        kicked_count (``int`` ``32-bit``, *optional*):
            N/A

        peer_link_requests_pending (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: list[str] = ["id", "about", "chat_photo", "linked_peers", "admins_count", "kicked_count", "peer_link_requests_pending"]

    ID = 0xcbb7a507
    QUALNAME = "types.CommunityFull"

    def __init__(self, *, id: int, about: str, chat_photo: raw.base.Photo, linked_peers: list[raw.base.CommunityPeer], admins_count: int | None = None, kicked_count: int | None = None, peer_link_requests_pending: int | None = None) -> None:
        self.id = id  # long
        self.about = about  # string
        self.chat_photo = chat_photo  # Photo
        self.linked_peers = linked_peers  # Vector<CommunityPeer>
        self.admins_count = admins_count  # flags.1?int
        self.kicked_count = kicked_count  # flags.2?int
        self.peer_link_requests_pending = peer_link_requests_pending  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> CommunityFull:
        
        flags = Int.read(b)
        
        id = Long.read(b)
        
        about = String.read(b)
        
        chat_photo = TLObject.read(b)
        
        linked_peers = TLObject.read(b)
        
        admins_count = Int.read(b) if flags & (1 << 1) else None
        kicked_count = Int.read(b) if flags & (1 << 2) else None
        peer_link_requests_pending = Int.read(b) if flags & (1 << 0) else None
        return CommunityFull(id=id, about=about, chat_photo=chat_photo, linked_peers=linked_peers, admins_count=admins_count, kicked_count=kicked_count, peer_link_requests_pending=peer_link_requests_pending)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.admins_count is not None else 0
        flags |= (1 << 2) if self.kicked_count is not None else 0
        flags |= (1 << 0) if self.peer_link_requests_pending is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(String(self.about))
        
        b.write(self.chat_photo.write())
        
        b.write(Vector(self.linked_peers))
        
        if self.admins_count is not None:
            b.write(Int(self.admins_count))
        
        if self.kicked_count is not None:
            b.write(Int(self.kicked_count))
        
        if self.peer_link_requests_pending is not None:
            b.write(Int(self.peer_link_requests_pending))
        
        return b.getvalue()
