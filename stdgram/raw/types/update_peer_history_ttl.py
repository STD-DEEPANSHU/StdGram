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


class UpdatePeerHistoryTTL(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.Update`.

    Details:
        - Layer: ``229``
        - ID: ``BB9BB9A5``

    Parameters:
        peer (:obj:`Peer <stdgram.raw.base.Peer>`):
            N/A

        ttl_period (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: list[str] = ["peer", "ttl_period"]

    ID = 0xbb9bb9a5
    QUALNAME = "types.UpdatePeerHistoryTTL"

    def __init__(self, *, peer: raw.base.Peer, ttl_period: int | None = None) -> None:
        self.peer = peer  # Peer
        self.ttl_period = ttl_period  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdatePeerHistoryTTL:
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        ttl_period = Int.read(b) if flags & (1 << 0) else None
        return UpdatePeerHistoryTTL(peer=peer, ttl_period=ttl_period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.ttl_period is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))
        
        return b.getvalue()
