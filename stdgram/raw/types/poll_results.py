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


class PollResults(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.PollResults`.

    Details:
        - Layer: ``229``
        - ID: ``BA7BB15E``

    Parameters:
        min (``bool``, *optional*):
            N/A

        has_unread_votes (``bool``, *optional*):
            N/A

        can_view_stats (``bool``, *optional*):
            N/A

        results (List of :obj:`PollAnswerVoters <stdgram.raw.base.PollAnswerVoters>`, *optional*):
            N/A

        total_voters (``int`` ``32-bit``, *optional*):
            N/A

        recent_voters (List of :obj:`Peer <stdgram.raw.base.Peer>`, *optional*):
            N/A

        solution (``str``, *optional*):
            N/A

        solution_entities (List of :obj:`MessageEntity <stdgram.raw.base.MessageEntity>`, *optional*):
            N/A

        solution_media (:obj:`MessageMedia <stdgram.raw.base.MessageMedia>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["min", "has_unread_votes", "can_view_stats", "results", "total_voters", "recent_voters", "solution", "solution_entities", "solution_media"]

    ID = 0xba7bb15e
    QUALNAME = "types.PollResults"

    def __init__(self, *, min: bool | None = None, has_unread_votes: bool | None = None, can_view_stats: bool | None = None, results: list[raw.base.PollAnswerVoters] | None = None, total_voters: int | None = None, recent_voters: list[raw.base.Peer] | None = None, solution: str | None = None, solution_entities: list[raw.base.MessageEntity] | None = None, solution_media: raw.base.MessageMedia | None = None) -> None:
        self.min = min  # flags.0?true
        self.has_unread_votes = has_unread_votes  # flags.6?true
        self.can_view_stats = can_view_stats  # flags.7?true
        self.results = results  # flags.1?Vector<PollAnswerVoters>
        self.total_voters = total_voters  # flags.2?int
        self.recent_voters = recent_voters  # flags.3?Vector<Peer>
        self.solution = solution  # flags.4?string
        self.solution_entities = solution_entities  # flags.4?Vector<MessageEntity>
        self.solution_media = solution_media  # flags.5?MessageMedia

    @staticmethod
    def read(b: BytesIO, *args: Any) -> PollResults:
        
        flags = Int.read(b)
        
        min = True if flags & (1 << 0) else False
        has_unread_votes = True if flags & (1 << 6) else False
        can_view_stats = True if flags & (1 << 7) else False
        results = TLObject.read(b) if flags & (1 << 1) else []
        
        total_voters = Int.read(b) if flags & (1 << 2) else None
        recent_voters = TLObject.read(b) if flags & (1 << 3) else []
        
        solution = String.read(b) if flags & (1 << 4) else None
        solution_entities = TLObject.read(b) if flags & (1 << 4) else []
        
        solution_media = TLObject.read(b) if flags & (1 << 5) else None
        
        return PollResults(min=min, has_unread_votes=has_unread_votes, can_view_stats=can_view_stats, results=results, total_voters=total_voters, recent_voters=recent_voters, solution=solution, solution_entities=solution_entities, solution_media=solution_media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.min else 0
        flags |= (1 << 6) if self.has_unread_votes else 0
        flags |= (1 << 7) if self.can_view_stats else 0
        flags |= (1 << 1) if self.results else 0
        flags |= (1 << 2) if self.total_voters is not None else 0
        flags |= (1 << 3) if self.recent_voters else 0
        flags |= (1 << 4) if self.solution is not None else 0
        flags |= (1 << 4) if self.solution_entities else 0
        flags |= (1 << 5) if self.solution_media is not None else 0
        b.write(Int(flags))
        
        if self.results is not None:
            b.write(Vector(self.results))
        
        if self.total_voters is not None:
            b.write(Int(self.total_voters))
        
        if self.recent_voters is not None:
            b.write(Vector(self.recent_voters))
        
        if self.solution is not None:
            b.write(String(self.solution))
        
        if self.solution_entities is not None:
            b.write(Vector(self.solution_entities))
        
        if self.solution_media is not None:
            b.write(self.solution_media.write())
        
        return b.getvalue()
