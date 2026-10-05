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


class ResPQ(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.ResPQ`.

    Details:
        - Layer: ``229``
        - ID: ``05162463``

    Parameters:
        nonce (``int`` ``128-bit``):
            N/A

        server_nonce (``int`` ``128-bit``):
            N/A

        pq (``bytes``):
            N/A

        server_public_key_fingerprints (List of ``int`` ``64-bit``):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            ReqPq
            ReqPqMulti
    """

    __slots__: list[str] = ["nonce", "server_nonce", "pq", "server_public_key_fingerprints"]

    ID = 0x05162463
    QUALNAME = "types.ResPQ"

    def __init__(self, *, nonce: int, server_nonce: int, pq: bytes, server_public_key_fingerprints: list[int]) -> None:
        self.nonce = nonce  # int128
        self.server_nonce = server_nonce  # int128
        self.pq = pq  # bytes
        self.server_public_key_fingerprints = server_public_key_fingerprints  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> ResPQ:
        # No flags
        
        nonce = Int128.read(b)
        
        server_nonce = Int128.read(b)
        
        pq = Bytes.read(b)
        
        server_public_key_fingerprints = TLObject.read(b, Long)
        
        return ResPQ(nonce=nonce, server_nonce=server_nonce, pq=pq, server_public_key_fingerprints=server_public_key_fingerprints)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int128(self.nonce))
        
        b.write(Int128(self.server_nonce))
        
        b.write(Bytes(self.pq))
        
        b.write(Vector(self.server_public_key_fingerprints, Long))
        
        return b.getvalue()
