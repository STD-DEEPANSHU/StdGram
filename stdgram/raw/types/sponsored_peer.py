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


class SponsoredPeer(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.SponsoredPeer`.

    Details:
        - Layer: ``229``
        - ID: ``C69708D3``

    Parameters:
        random_id (``bytes``):
            N/A

        peer (:obj:`Peer <stdgram.raw.base.Peer>`):
            N/A

        sponsor_info (``str``, *optional*):
            N/A

        additional_info (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["random_id", "peer", "sponsor_info", "additional_info"]

    ID = 0xc69708d3
    QUALNAME = "types.SponsoredPeer"

    def __init__(self, *, random_id: bytes, peer: raw.base.Peer, sponsor_info: str | None = None, additional_info: str | None = None) -> None:
        self.random_id = random_id  # bytes
        self.peer = peer  # Peer
        self.sponsor_info = sponsor_info  # flags.0?string
        self.additional_info = additional_info  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SponsoredPeer:
        
        flags = Int.read(b)
        
        random_id = Bytes.read(b)
        
        peer = TLObject.read(b)
        
        sponsor_info = String.read(b) if flags & (1 << 0) else None
        additional_info = String.read(b) if flags & (1 << 1) else None
        return SponsoredPeer(random_id=random_id, peer=peer, sponsor_info=sponsor_info, additional_info=additional_info)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.sponsor_info is not None else 0
        flags |= (1 << 1) if self.additional_info is not None else 0
        b.write(Int(flags))
        
        b.write(Bytes(self.random_id))
        
        b.write(self.peer.write())
        
        if self.sponsor_info is not None:
            b.write(String(self.sponsor_info))
        
        if self.additional_info is not None:
            b.write(String(self.additional_info))
        
        return b.getvalue()
