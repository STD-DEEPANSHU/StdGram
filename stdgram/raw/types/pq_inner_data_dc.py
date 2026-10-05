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


class PQInnerDataDc(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.PQInnerData`.

    Details:
        - Layer: ``229``
        - ID: ``A9F55F95``

    Parameters:
        pq (``bytes``):
            N/A

        p (``bytes``):
            N/A

        q (``bytes``):
            N/A

        nonce (``int`` ``128-bit``):
            N/A

        server_nonce (``int`` ``128-bit``):
            N/A

        new_nonce (``int`` ``256-bit``):
            N/A

        dc (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["pq", "p", "q", "nonce", "server_nonce", "new_nonce", "dc"]

    ID = 0xa9f55f95
    QUALNAME = "types.PQInnerDataDc"

    def __init__(self, *, pq: bytes, p: bytes, q: bytes, nonce: int, server_nonce: int, new_nonce: int, dc: int) -> None:
        self.pq = pq  # bytes
        self.p = p  # bytes
        self.q = q  # bytes
        self.nonce = nonce  # int128
        self.server_nonce = server_nonce  # int128
        self.new_nonce = new_nonce  # int256
        self.dc = dc  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> PQInnerDataDc:
        # No flags
        
        pq = Bytes.read(b)
        
        p = Bytes.read(b)
        
        q = Bytes.read(b)
        
        nonce = Int128.read(b)
        
        server_nonce = Int128.read(b)
        
        new_nonce = Int256.read(b)
        
        dc = Int.read(b)
        
        return PQInnerDataDc(pq=pq, p=p, q=q, nonce=nonce, server_nonce=server_nonce, new_nonce=new_nonce, dc=dc)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.pq))
        
        b.write(Bytes(self.p))
        
        b.write(Bytes(self.q))
        
        b.write(Int128(self.nonce))
        
        b.write(Int128(self.server_nonce))
        
        b.write(Int256(self.new_nonce))
        
        b.write(Int(self.dc))
        
        return b.getvalue()
