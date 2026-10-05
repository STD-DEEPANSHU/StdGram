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


class GetParticipantJoinedChats(TLObject["raw.base.communities.ParticipantJoinedChats"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``F87EABAB``

    Parameters:
        community (:obj:`InputChannel <stdgram.raw.base.InputChannel>`):
            N/A

        participant (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

    Returns:
        :obj:`communities.ParticipantJoinedChats <stdgram.raw.base.communities.ParticipantJoinedChats>`
    """

    __slots__: list[str] = ["community", "participant"]

    ID = 0xf87eabab
    QUALNAME = "functions.communities.GetParticipantJoinedChats"

    def __init__(self, *, community: raw.base.InputChannel, participant: raw.base.InputPeer) -> None:
        self.community = community  # InputChannel
        self.participant = participant  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GetParticipantJoinedChats:
        # No flags
        
        community = TLObject.read(b)
        
        participant = TLObject.read(b)
        
        return GetParticipantJoinedChats(community=community, participant=participant)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.community.write())
        
        b.write(self.participant.write())
        
        return b.getvalue()
