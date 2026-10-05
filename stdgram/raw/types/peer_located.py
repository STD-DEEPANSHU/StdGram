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


class PeerLocated(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.PeerLocated`.

    Details:
        - Layer: ``229``
        - ID: ``CA461B5D``

    Parameters:
        peer (:obj:`Peer <stdgram.raw.base.Peer>`):
            N/A

        expires (``int`` ``32-bit``):
            N/A

        distance (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["peer", "expires", "distance"]

    ID = 0xca461b5d
    QUALNAME = "types.PeerLocated"

    def __init__(self, *, peer: raw.base.Peer, expires: int, distance: int) -> None:
        self.peer = peer  # Peer
        self.expires = expires  # int
        self.distance = distance  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> PeerLocated:
        # No flags
        
        peer = TLObject.read(b)
        
        expires = Int.read(b)
        
        distance = Int.read(b)
        
        return PeerLocated(peer=peer, expires=expires, distance=distance)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.expires))
        
        b.write(Int(self.distance))
        
        return b.getvalue()
