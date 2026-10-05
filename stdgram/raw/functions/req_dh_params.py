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


class ReqDHParams(TLObject["raw.base.ServerDHParams"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``D712E4BE``

    Parameters:
        nonce (``int`` ``128-bit``):
            N/A

        server_nonce (``int`` ``128-bit``):
            N/A

        p (``bytes``):
            N/A

        q (``bytes``):
            N/A

        public_key_fingerprint (``int`` ``64-bit``):
            N/A

        encrypted_data (``bytes``):
            N/A

    Returns:
        :obj:`ServerDHParams <stdgram.raw.base.ServerDHParams>`
    """

    __slots__: list[str] = ["nonce", "server_nonce", "p", "q", "public_key_fingerprint", "encrypted_data"]

    ID = 0xd712e4be
    QUALNAME = "functions.ReqDHParams"

    def __init__(self, *, nonce: int, server_nonce: int, p: bytes, q: bytes, public_key_fingerprint: int, encrypted_data: bytes) -> None:
        self.nonce = nonce  # int128
        self.server_nonce = server_nonce  # int128
        self.p = p  # bytes
        self.q = q  # bytes
        self.public_key_fingerprint = public_key_fingerprint  # long
        self.encrypted_data = encrypted_data  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> ReqDHParams:
        # No flags
        
        nonce = Int128.read(b)
        
        server_nonce = Int128.read(b)
        
        p = Bytes.read(b)
        
        q = Bytes.read(b)
        
        public_key_fingerprint = Long.read(b)
        
        encrypted_data = Bytes.read(b)
        
        return ReqDHParams(nonce=nonce, server_nonce=server_nonce, p=p, q=q, public_key_fingerprint=public_key_fingerprint, encrypted_data=encrypted_data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int128(self.nonce))
        
        b.write(Int128(self.server_nonce))
        
        b.write(Bytes(self.p))
        
        b.write(Bytes(self.q))
        
        b.write(Long(self.public_key_fingerprint))
        
        b.write(Bytes(self.encrypted_data))
        
        return b.getvalue()
