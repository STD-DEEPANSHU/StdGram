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


class SendBotRequestedPeer(TLObject["raw.base.Updates"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``6C5CF2A7``

    Parameters:
        peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        button_id (``int`` ``32-bit``):
            N/A

        requested_peers (List of :obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        msg_id (``int`` ``32-bit``, *optional*):
            N/A

        webapp_req_id (``str``, *optional*):
            N/A

    Returns:
        :obj:`Updates <stdgram.raw.base.Updates>`
    """

    __slots__: list[str] = ["peer", "button_id", "requested_peers", "msg_id", "webapp_req_id"]

    ID = 0x6c5cf2a7
    QUALNAME = "functions.messages.SendBotRequestedPeer"

    def __init__(self, *, peer: raw.base.InputPeer, button_id: int, requested_peers: list[raw.base.InputPeer], msg_id: int | None = None, webapp_req_id: str | None = None) -> None:
        self.peer = peer  # InputPeer
        self.button_id = button_id  # int
        self.requested_peers = requested_peers  # Vector<InputPeer>
        self.msg_id = msg_id  # flags.0?int
        self.webapp_req_id = webapp_req_id  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SendBotRequestedPeer:
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        msg_id = Int.read(b) if flags & (1 << 0) else None
        webapp_req_id = String.read(b) if flags & (1 << 1) else None
        button_id = Int.read(b)
        
        requested_peers = TLObject.read(b)
        
        return SendBotRequestedPeer(peer=peer, button_id=button_id, requested_peers=requested_peers, msg_id=msg_id, webapp_req_id=webapp_req_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.msg_id is not None else 0
        flags |= (1 << 1) if self.webapp_req_id is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.msg_id is not None:
            b.write(Int(self.msg_id))
        
        if self.webapp_req_id is not None:
            b.write(String(self.webapp_req_id))
        
        b.write(Int(self.button_id))
        
        b.write(Vector(self.requested_peers))
        
        return b.getvalue()
