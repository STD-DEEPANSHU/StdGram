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


class UpdateNewStoryReaction(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.Update`.

    Details:
        - Layer: ``229``
        - ID: ``1824E40B``

    Parameters:
        story_id (``int`` ``32-bit``):
            N/A

        peer (:obj:`Peer <stdgram.raw.base.Peer>`):
            N/A

        reaction (:obj:`Reaction <stdgram.raw.base.Reaction>`):
            N/A

    """

    __slots__: list[str] = ["story_id", "peer", "reaction"]

    ID = 0x1824e40b
    QUALNAME = "types.UpdateNewStoryReaction"

    def __init__(self, *, story_id: int, peer: raw.base.Peer, reaction: raw.base.Reaction) -> None:
        self.story_id = story_id  # int
        self.peer = peer  # Peer
        self.reaction = reaction  # Reaction

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateNewStoryReaction:
        # No flags
        
        story_id = Int.read(b)
        
        peer = TLObject.read(b)
        
        reaction = TLObject.read(b)
        
        return UpdateNewStoryReaction(story_id=story_id, peer=peer, reaction=reaction)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.story_id))
        
        b.write(self.peer.write())
        
        b.write(self.reaction.write())
        
        return b.getvalue()
