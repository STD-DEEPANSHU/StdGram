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


class ConfirmCall(TLObject["raw.base.phone.PhoneCall"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``2EFE1722``

    Parameters:
        peer (:obj:`InputPhoneCall <stdgram.raw.base.InputPhoneCall>`):
            N/A

        g_a (``bytes``):
            N/A

        key_fingerprint (``int`` ``64-bit``):
            N/A

        protocol (:obj:`PhoneCallProtocol <stdgram.raw.base.PhoneCallProtocol>`):
            N/A

    Returns:
        :obj:`phone.PhoneCall <stdgram.raw.base.phone.PhoneCall>`
    """

    __slots__: list[str] = ["peer", "g_a", "key_fingerprint", "protocol"]

    ID = 0x2efe1722
    QUALNAME = "functions.phone.ConfirmCall"

    def __init__(self, *, peer: raw.base.InputPhoneCall, g_a: bytes, key_fingerprint: int, protocol: raw.base.PhoneCallProtocol) -> None:
        self.peer = peer  # InputPhoneCall
        self.g_a = g_a  # bytes
        self.key_fingerprint = key_fingerprint  # long
        self.protocol = protocol  # PhoneCallProtocol

    @staticmethod
    def read(b: BytesIO, *args: Any) -> ConfirmCall:
        # No flags
        
        peer = TLObject.read(b)
        
        g_a = Bytes.read(b)
        
        key_fingerprint = Long.read(b)
        
        protocol = TLObject.read(b)
        
        return ConfirmCall(peer=peer, g_a=g_a, key_fingerprint=key_fingerprint, protocol=protocol)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Bytes(self.g_a))
        
        b.write(Long(self.key_fingerprint))
        
        b.write(self.protocol.write())
        
        return b.getvalue()
