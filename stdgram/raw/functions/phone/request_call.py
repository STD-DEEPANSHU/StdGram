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


class RequestCall(TLObject["raw.base.phone.PhoneCall"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``42FF96ED``

    Parameters:
        user_id (:obj:`InputUser <stdgram.raw.base.InputUser>`):
            N/A

        random_id (``int`` ``32-bit``):
            N/A

        g_a_hash (``bytes``):
            N/A

        protocol (:obj:`PhoneCallProtocol <stdgram.raw.base.PhoneCallProtocol>`):
            N/A

        video (``bool``, *optional*):
            N/A

    Returns:
        :obj:`phone.PhoneCall <stdgram.raw.base.phone.PhoneCall>`
    """

    __slots__: list[str] = ["user_id", "random_id", "g_a_hash", "protocol", "video"]

    ID = 0x42ff96ed
    QUALNAME = "functions.phone.RequestCall"

    def __init__(self, *, user_id: raw.base.InputUser, random_id: int, g_a_hash: bytes, protocol: raw.base.PhoneCallProtocol, video: bool | None = None) -> None:
        self.user_id = user_id  # InputUser
        self.random_id = random_id  # int
        self.g_a_hash = g_a_hash  # bytes
        self.protocol = protocol  # PhoneCallProtocol
        self.video = video  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> RequestCall:
        
        flags = Int.read(b)
        
        video = True if flags & (1 << 0) else False
        user_id = TLObject.read(b)
        
        random_id = Int.read(b)
        
        g_a_hash = Bytes.read(b)
        
        protocol = TLObject.read(b)
        
        return RequestCall(user_id=user_id, random_id=random_id, g_a_hash=g_a_hash, protocol=protocol, video=video)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.video else 0
        b.write(Int(flags))
        
        b.write(self.user_id.write())
        
        b.write(Int(self.random_id))
        
        b.write(Bytes(self.g_a_hash))
        
        b.write(self.protocol.write())
        
        return b.getvalue()
