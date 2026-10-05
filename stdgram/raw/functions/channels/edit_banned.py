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


class EditBanned(TLObject["raw.base.Updates"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``96E6CD81``

    Parameters:
        channel (:obj:`InputChannel <stdgram.raw.base.InputChannel>`):
            N/A

        participant (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        banned_rights (:obj:`ChatBannedRights <stdgram.raw.base.ChatBannedRights>`):
            N/A

    Returns:
        :obj:`Updates <stdgram.raw.base.Updates>`
    """

    __slots__: list[str] = ["channel", "participant", "banned_rights"]

    ID = 0x96e6cd81
    QUALNAME = "functions.channels.EditBanned"

    def __init__(self, *, channel: raw.base.InputChannel, participant: raw.base.InputPeer, banned_rights: raw.base.ChatBannedRights) -> None:
        self.channel = channel  # InputChannel
        self.participant = participant  # InputPeer
        self.banned_rights = banned_rights  # ChatBannedRights

    @staticmethod
    def read(b: BytesIO, *args: Any) -> EditBanned:
        # No flags
        
        channel = TLObject.read(b)
        
        participant = TLObject.read(b)
        
        banned_rights = TLObject.read(b)
        
        return EditBanned(channel=channel, participant=participant, banned_rights=banned_rights)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(self.participant.write())
        
        b.write(self.banned_rights.write())
        
        return b.getvalue()
