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


class MessageReactions(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.MessageReactions`.

    Details:
        - Layer: ``229``
        - ID: ``A339F0B``

    Parameters:
        results (List of :obj:`ReactionCount <stdgram.raw.base.ReactionCount>`):
            N/A

        min (``bool``, *optional*):
            N/A

        can_see_list (``bool``, *optional*):
            N/A

        reactions_as_tags (``bool``, *optional*):
            N/A

        recent_reactions (List of :obj:`MessagePeerReaction <stdgram.raw.base.MessagePeerReaction>`, *optional*):
            N/A

        top_reactors (List of :obj:`MessageReactor <stdgram.raw.base.MessageReactor>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["results", "min", "can_see_list", "reactions_as_tags", "recent_reactions", "top_reactors"]

    ID = 0xa339f0b
    QUALNAME = "types.MessageReactions"

    def __init__(self, *, results: list[raw.base.ReactionCount], min: bool | None = None, can_see_list: bool | None = None, reactions_as_tags: bool | None = None, recent_reactions: list[raw.base.MessagePeerReaction] | None = None, top_reactors: list[raw.base.MessageReactor] | None = None) -> None:
        self.results = results  # Vector<ReactionCount>
        self.min = min  # flags.0?true
        self.can_see_list = can_see_list  # flags.2?true
        self.reactions_as_tags = reactions_as_tags  # flags.3?true
        self.recent_reactions = recent_reactions  # flags.1?Vector<MessagePeerReaction>
        self.top_reactors = top_reactors  # flags.4?Vector<MessageReactor>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> MessageReactions:
        
        flags = Int.read(b)
        
        min = True if flags & (1 << 0) else False
        can_see_list = True if flags & (1 << 2) else False
        reactions_as_tags = True if flags & (1 << 3) else False
        results = TLObject.read(b)
        
        recent_reactions = TLObject.read(b) if flags & (1 << 1) else []
        
        top_reactors = TLObject.read(b) if flags & (1 << 4) else []
        
        return MessageReactions(results=results, min=min, can_see_list=can_see_list, reactions_as_tags=reactions_as_tags, recent_reactions=recent_reactions, top_reactors=top_reactors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.min else 0
        flags |= (1 << 2) if self.can_see_list else 0
        flags |= (1 << 3) if self.reactions_as_tags else 0
        flags |= (1 << 1) if self.recent_reactions else 0
        flags |= (1 << 4) if self.top_reactors else 0
        b.write(Int(flags))
        
        b.write(Vector(self.results))
        
        if self.recent_reactions is not None:
            b.write(Vector(self.recent_reactions))
        
        if self.top_reactors is not None:
            b.write(Vector(self.top_reactors))
        
        return b.getvalue()
