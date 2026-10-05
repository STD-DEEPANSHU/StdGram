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


class UpdateChannelParticipant(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.Update`.

    Details:
        - Layer: ``229``
        - ID: ``985D3ABB``

    Parameters:
        channel_id (``int`` ``64-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        actor_id (``int`` ``64-bit``):
            N/A

        user_id (``int`` ``64-bit``):
            N/A

        qts (``int`` ``32-bit``):
            N/A

        via_chatlist (``bool``, *optional*):
            N/A

        prev_participant (:obj:`ChannelParticipant <stdgram.raw.base.ChannelParticipant>`, *optional*):
            N/A

        new_participant (:obj:`ChannelParticipant <stdgram.raw.base.ChannelParticipant>`, *optional*):
            N/A

        invite (:obj:`ExportedChatInvite <stdgram.raw.base.ExportedChatInvite>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["channel_id", "date", "actor_id", "user_id", "qts", "via_chatlist", "prev_participant", "new_participant", "invite"]

    ID = 0x985d3abb
    QUALNAME = "types.UpdateChannelParticipant"

    def __init__(self, *, channel_id: int, date: int, actor_id: int, user_id: int, qts: int, via_chatlist: bool | None = None, prev_participant: raw.base.ChannelParticipant | None = None, new_participant: raw.base.ChannelParticipant | None = None, invite: raw.base.ExportedChatInvite | None = None) -> None:
        self.channel_id = channel_id  # long
        self.date = date  # int
        self.actor_id = actor_id  # long
        self.user_id = user_id  # long
        self.qts = qts  # int
        self.via_chatlist = via_chatlist  # flags.3?true
        self.prev_participant = prev_participant  # flags.0?ChannelParticipant
        self.new_participant = new_participant  # flags.1?ChannelParticipant
        self.invite = invite  # flags.2?ExportedChatInvite

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateChannelParticipant:
        
        flags = Int.read(b)
        
        via_chatlist = True if flags & (1 << 3) else False
        channel_id = Long.read(b)
        
        date = Int.read(b)
        
        actor_id = Long.read(b)
        
        user_id = Long.read(b)
        
        prev_participant = TLObject.read(b) if flags & (1 << 0) else None
        
        new_participant = TLObject.read(b) if flags & (1 << 1) else None
        
        invite = TLObject.read(b) if flags & (1 << 2) else None
        
        qts = Int.read(b)
        
        return UpdateChannelParticipant(channel_id=channel_id, date=date, actor_id=actor_id, user_id=user_id, qts=qts, via_chatlist=via_chatlist, prev_participant=prev_participant, new_participant=new_participant, invite=invite)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.via_chatlist else 0
        flags |= (1 << 0) if self.prev_participant is not None else 0
        flags |= (1 << 1) if self.new_participant is not None else 0
        flags |= (1 << 2) if self.invite is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.channel_id))
        
        b.write(Int(self.date))
        
        b.write(Long(self.actor_id))
        
        b.write(Long(self.user_id))
        
        if self.prev_participant is not None:
            b.write(self.prev_participant.write())
        
        if self.new_participant is not None:
            b.write(self.new_participant.write())
        
        if self.invite is not None:
            b.write(self.invite.write())
        
        b.write(Int(self.qts))
        
        return b.getvalue()
