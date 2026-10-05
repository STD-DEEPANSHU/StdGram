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


class MessageStats(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.stats.MessageStats`.

    Details:
        - Layer: ``229``
        - ID: ``7FE91C14``

    Parameters:
        views_graph (:obj:`StatsGraph <stdgram.raw.base.StatsGraph>`):
            N/A

        reactions_by_emotion_graph (:obj:`StatsGraph <stdgram.raw.base.StatsGraph>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            stats.GetMessageStats
    """

    __slots__: list[str] = ["views_graph", "reactions_by_emotion_graph"]

    ID = 0x7fe91c14
    QUALNAME = "types.stats.MessageStats"

    def __init__(self, *, views_graph: raw.base.StatsGraph, reactions_by_emotion_graph: raw.base.StatsGraph) -> None:
        self.views_graph = views_graph  # StatsGraph
        self.reactions_by_emotion_graph = reactions_by_emotion_graph  # StatsGraph

    @staticmethod
    def read(b: BytesIO, *args: Any) -> MessageStats:
        # No flags
        
        views_graph = TLObject.read(b)
        
        reactions_by_emotion_graph = TLObject.read(b)
        
        return MessageStats(views_graph=views_graph, reactions_by_emotion_graph=reactions_by_emotion_graph)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.views_graph.write())
        
        b.write(self.reactions_by_emotion_graph.write())
        
        return b.getvalue()
