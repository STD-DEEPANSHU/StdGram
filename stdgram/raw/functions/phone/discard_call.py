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


class DiscardCall(TLObject["raw.base.Updates"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``B2CBC1C0``

    Parameters:
        peer (:obj:`InputPhoneCall <stdgram.raw.base.InputPhoneCall>`):
            N/A

        duration (``int`` ``32-bit``):
            N/A

        reason (:obj:`PhoneCallDiscardReason <stdgram.raw.base.PhoneCallDiscardReason>`):
            N/A

        connection_id (``int`` ``64-bit``):
            N/A

        video (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <stdgram.raw.base.Updates>`
    """

    __slots__: list[str] = ["peer", "duration", "reason", "connection_id", "video"]

    ID = 0xb2cbc1c0
    QUALNAME = "functions.phone.DiscardCall"

    def __init__(self, *, peer: raw.base.InputPhoneCall, duration: int, reason: raw.base.PhoneCallDiscardReason, connection_id: int, video: bool | None = None) -> None:
        self.peer = peer  # InputPhoneCall
        self.duration = duration  # int
        self.reason = reason  # PhoneCallDiscardReason
        self.connection_id = connection_id  # long
        self.video = video  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> DiscardCall:
        
        flags = Int.read(b)
        
        video = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        duration = Int.read(b)
        
        reason = TLObject.read(b)
        
        connection_id = Long.read(b)
        
        return DiscardCall(peer=peer, duration=duration, reason=reason, connection_id=connection_id, video=video)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.video else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.duration))
        
        b.write(self.reason.write())
        
        b.write(Long(self.connection_id))
        
        return b.getvalue()
