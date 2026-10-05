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


class SendGroupCallMessage(TLObject["raw.base.Updates"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``B1D11410``

    Parameters:
        call (:obj:`InputGroupCall <stdgram.raw.base.InputGroupCall>`):
            N/A

        random_id (``int`` ``64-bit``):
            N/A

        message (:obj:`TextWithEntities <stdgram.raw.base.TextWithEntities>`):
            N/A

        allow_paid_stars (``int`` ``64-bit``, *optional*):
            N/A

        send_as (:obj:`InputPeer <stdgram.raw.base.InputPeer>`, *optional*):
            N/A

    Returns:
        :obj:`Updates <stdgram.raw.base.Updates>`
    """

    __slots__: list[str] = ["call", "random_id", "message", "allow_paid_stars", "send_as"]

    ID = 0xb1d11410
    QUALNAME = "functions.phone.SendGroupCallMessage"

    def __init__(self, *, call: raw.base.InputGroupCall, random_id: int, message: raw.base.TextWithEntities, allow_paid_stars: int | None = None, send_as: raw.base.InputPeer | None = None) -> None:
        self.call = call  # InputGroupCall
        self.random_id = random_id  # long
        self.message = message  # TextWithEntities
        self.allow_paid_stars = allow_paid_stars  # flags.0?long
        self.send_as = send_as  # flags.1?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SendGroupCallMessage:
        
        flags = Int.read(b)
        
        call = TLObject.read(b)
        
        random_id = Long.read(b)
        
        message = TLObject.read(b)
        
        allow_paid_stars = Long.read(b) if flags & (1 << 0) else None
        send_as = TLObject.read(b) if flags & (1 << 1) else None
        
        return SendGroupCallMessage(call=call, random_id=random_id, message=message, allow_paid_stars=allow_paid_stars, send_as=send_as)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.allow_paid_stars is not None else 0
        flags |= (1 << 1) if self.send_as is not None else 0
        b.write(Int(flags))
        
        b.write(self.call.write())
        
        b.write(Long(self.random_id))
        
        b.write(self.message.write())
        
        if self.allow_paid_stars is not None:
            b.write(Long(self.allow_paid_stars))
        
        if self.send_as is not None:
            b.write(self.send_as.write())
        
        return b.getvalue()
