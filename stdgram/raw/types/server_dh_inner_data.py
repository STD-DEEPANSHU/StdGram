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


class ServerDHInnerData(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.ServerDHInnerData`.

    Details:
        - Layer: ``229``
        - ID: ``B5890DBA``

    Parameters:
        nonce (``int`` ``128-bit``):
            N/A

        server_nonce (``int`` ``128-bit``):
            N/A

        g (``int`` ``32-bit``):
            N/A

        dh_prime (``bytes``):
            N/A

        g_a (``bytes``):
            N/A

        server_time (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["nonce", "server_nonce", "g", "dh_prime", "g_a", "server_time"]

    ID = 0xb5890dba
    QUALNAME = "types.ServerDHInnerData"

    def __init__(self, *, nonce: int, server_nonce: int, g: int, dh_prime: bytes, g_a: bytes, server_time: int) -> None:
        self.nonce = nonce  # int128
        self.server_nonce = server_nonce  # int128
        self.g = g  # int
        self.dh_prime = dh_prime  # bytes
        self.g_a = g_a  # bytes
        self.server_time = server_time  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> ServerDHInnerData:
        # No flags
        
        nonce = Int128.read(b)
        
        server_nonce = Int128.read(b)
        
        g = Int.read(b)
        
        dh_prime = Bytes.read(b)
        
        g_a = Bytes.read(b)
        
        server_time = Int.read(b)
        
        return ServerDHInnerData(nonce=nonce, server_nonce=server_nonce, g=g, dh_prime=dh_prime, g_a=g_a, server_time=server_time)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int128(self.nonce))
        
        b.write(Int128(self.server_nonce))
        
        b.write(Int(self.g))
        
        b.write(Bytes(self.dh_prime))
        
        b.write(Bytes(self.g_a))
        
        b.write(Int(self.server_time))
        
        return b.getvalue()
