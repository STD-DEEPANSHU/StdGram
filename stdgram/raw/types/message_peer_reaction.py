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


class MessagePeerReaction(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.MessagePeerReaction`.

    Details:
        - Layer: ``229``
        - ID: ``8C79B63C``

    Parameters:
        peer_id (:obj:`Peer <stdgram.raw.base.Peer>`):
            N/A

        date (``int`` ``32-bit``):
            N/A

        reaction (:obj:`Reaction <stdgram.raw.base.Reaction>`):
            N/A

        big (``bool``, *optional*):
            N/A

        unread (``bool``, *optional*):
            N/A

        my (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["peer_id", "date", "reaction", "big", "unread", "my"]

    ID = 0x8c79b63c
    QUALNAME = "types.MessagePeerReaction"

    def __init__(self, *, peer_id: raw.base.Peer, date: int, reaction: raw.base.Reaction, big: bool | None = None, unread: bool | None = None, my: bool | None = None) -> None:
        self.peer_id = peer_id  # Peer
        self.date = date  # int
        self.reaction = reaction  # Reaction
        self.big = big  # flags.0?true
        self.unread = unread  # flags.1?true
        self.my = my  # flags.2?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> MessagePeerReaction:
        
        flags = Int.read(b)
        
        big = True if flags & (1 << 0) else False
        unread = True if flags & (1 << 1) else False
        my = True if flags & (1 << 2) else False
        peer_id = TLObject.read(b)
        
        date = Int.read(b)
        
        reaction = TLObject.read(b)
        
        return MessagePeerReaction(peer_id=peer_id, date=date, reaction=reaction, big=big, unread=unread, my=my)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.big else 0
        flags |= (1 << 1) if self.unread else 0
        flags |= (1 << 2) if self.my else 0
        b.write(Int(flags))
        
        b.write(self.peer_id.write())
        
        b.write(Int(self.date))
        
        b.write(self.reaction.write())
        
        return b.getvalue()
