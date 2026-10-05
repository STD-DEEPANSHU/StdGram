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


class GetSearchCounters(TLObject["list[raw.base.messages.SearchCounter]"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``1BBCF300``

    Parameters:
        peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        filters (List of :obj:`MessagesFilter <stdgram.raw.base.MessagesFilter>`):
            N/A

        saved_peer_id (:obj:`InputPeer <stdgram.raw.base.InputPeer>`, *optional*):
            N/A

        top_msg_id (``int`` ``32-bit``, *optional*):
            N/A

    Returns:
        List of :obj:`messages.SearchCounter <stdgram.raw.base.messages.SearchCounter>`
    """

    __slots__: list[str] = ["peer", "filters", "saved_peer_id", "top_msg_id"]

    ID = 0x1bbcf300
    QUALNAME = "functions.messages.GetSearchCounters"

    def __init__(self, *, peer: raw.base.InputPeer, filters: list[raw.base.MessagesFilter], saved_peer_id: raw.base.InputPeer | None = None, top_msg_id: int | None = None) -> None:
        self.peer = peer  # InputPeer
        self.filters = filters  # Vector<MessagesFilter>
        self.saved_peer_id = saved_peer_id  # flags.2?InputPeer
        self.top_msg_id = top_msg_id  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GetSearchCounters:
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        saved_peer_id = TLObject.read(b) if flags & (1 << 2) else None
        
        top_msg_id = Int.read(b) if flags & (1 << 0) else None
        filters = TLObject.read(b)
        
        return GetSearchCounters(peer=peer, filters=filters, saved_peer_id=saved_peer_id, top_msg_id=top_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.saved_peer_id is not None else 0
        flags |= (1 << 0) if self.top_msg_id is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.saved_peer_id is not None:
            b.write(self.saved_peer_id.write())
        
        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))
        
        b.write(Vector(self.filters))
        
        return b.getvalue()
