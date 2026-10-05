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


class GetStoryReactionsList(TLObject["raw.base.stories.StoryReactionsList"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``B9B2881F``

    Parameters:
        peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        id (``int`` ``32-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        forwards_first (``bool``, *optional*):
            N/A

        reaction (:obj:`Reaction <stdgram.raw.base.Reaction>`, *optional*):
            N/A

        offset (``str``, *optional*):
            N/A

    Returns:
        :obj:`stories.StoryReactionsList <stdgram.raw.base.stories.StoryReactionsList>`
    """

    __slots__: list[str] = ["peer", "id", "limit", "forwards_first", "reaction", "offset"]

    ID = 0xb9b2881f
    QUALNAME = "functions.stories.GetStoryReactionsList"

    def __init__(self, *, peer: raw.base.InputPeer, id: int, limit: int, forwards_first: bool | None = None, reaction: raw.base.Reaction | None = None, offset: str | None = None) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.limit = limit  # int
        self.forwards_first = forwards_first  # flags.2?true
        self.reaction = reaction  # flags.0?Reaction
        self.offset = offset  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GetStoryReactionsList:
        
        flags = Int.read(b)
        
        forwards_first = True if flags & (1 << 2) else False
        peer = TLObject.read(b)
        
        id = Int.read(b)
        
        reaction = TLObject.read(b) if flags & (1 << 0) else None
        
        offset = String.read(b) if flags & (1 << 1) else None
        limit = Int.read(b)
        
        return GetStoryReactionsList(peer=peer, id=id, limit=limit, forwards_first=forwards_first, reaction=reaction, offset=offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.forwards_first else 0
        flags |= (1 << 0) if self.reaction is not None else 0
        flags |= (1 << 1) if self.offset is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        if self.reaction is not None:
            b.write(self.reaction.write())
        
        if self.offset is not None:
            b.write(String(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
