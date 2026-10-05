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


class MessageActionConferenceCall(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.MessageAction`.

    Details:
        - Layer: ``229``
        - ID: ``2FFE2F7A``

    Parameters:
        call_id (``int`` ``64-bit``):
            N/A

        missed (``bool``, *optional*):
            N/A

        active (``bool``, *optional*):
            N/A

        video (``bool``, *optional*):
            N/A

        duration (``int`` ``32-bit``, *optional*):
            N/A

        other_participants (List of :obj:`Peer <stdgram.raw.base.Peer>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["call_id", "missed", "active", "video", "duration", "other_participants"]

    ID = 0x2ffe2f7a
    QUALNAME = "types.MessageActionConferenceCall"

    def __init__(self, *, call_id: int, missed: bool | None = None, active: bool | None = None, video: bool | None = None, duration: int | None = None, other_participants: list[raw.base.Peer] | None = None) -> None:
        self.call_id = call_id  # long
        self.missed = missed  # flags.0?true
        self.active = active  # flags.1?true
        self.video = video  # flags.4?true
        self.duration = duration  # flags.2?int
        self.other_participants = other_participants  # flags.3?Vector<Peer>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> MessageActionConferenceCall:
        
        flags = Int.read(b)
        
        missed = True if flags & (1 << 0) else False
        active = True if flags & (1 << 1) else False
        video = True if flags & (1 << 4) else False
        call_id = Long.read(b)
        
        duration = Int.read(b) if flags & (1 << 2) else None
        other_participants = TLObject.read(b) if flags & (1 << 3) else []
        
        return MessageActionConferenceCall(call_id=call_id, missed=missed, active=active, video=video, duration=duration, other_participants=other_participants)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.missed else 0
        flags |= (1 << 1) if self.active else 0
        flags |= (1 << 4) if self.video else 0
        flags |= (1 << 2) if self.duration is not None else 0
        flags |= (1 << 3) if self.other_participants else 0
        b.write(Int(flags))
        
        b.write(Long(self.call_id))
        
        if self.duration is not None:
            b.write(Int(self.duration))
        
        if self.other_participants is not None:
            b.write(Vector(self.other_participants))
        
        return b.getvalue()
