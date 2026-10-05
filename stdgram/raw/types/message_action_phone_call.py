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


class MessageActionPhoneCall(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.MessageAction`.

    Details:
        - Layer: ``229``
        - ID: ``80E11A7F``

    Parameters:
        call_id (``int`` ``64-bit``):
            N/A

        video (``bool``, *optional*):
            N/A

        reason (:obj:`PhoneCallDiscardReason <stdgram.raw.base.PhoneCallDiscardReason>`, *optional*):
            N/A

        duration (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: list[str] = ["call_id", "video", "reason", "duration"]

    ID = 0x80e11a7f
    QUALNAME = "types.MessageActionPhoneCall"

    def __init__(self, *, call_id: int, video: bool | None = None, reason: raw.base.PhoneCallDiscardReason | None = None, duration: int | None = None) -> None:
        self.call_id = call_id  # long
        self.video = video  # flags.2?true
        self.reason = reason  # flags.0?PhoneCallDiscardReason
        self.duration = duration  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> MessageActionPhoneCall:
        
        flags = Int.read(b)
        
        video = True if flags & (1 << 2) else False
        call_id = Long.read(b)
        
        reason = TLObject.read(b) if flags & (1 << 0) else None
        
        duration = Int.read(b) if flags & (1 << 1) else None
        return MessageActionPhoneCall(call_id=call_id, video=video, reason=reason, duration=duration)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.video else 0
        flags |= (1 << 0) if self.reason is not None else 0
        flags |= (1 << 1) if self.duration is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.call_id))
        
        if self.reason is not None:
            b.write(self.reason.write())
        
        if self.duration is not None:
            b.write(Int(self.duration))
        
        return b.getvalue()
