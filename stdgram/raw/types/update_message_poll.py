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


class UpdateMessagePoll(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.Update`.

    Details:
        - Layer: ``229``
        - ID: ``D64C522B``

    Parameters:
        poll_id (``int`` ``64-bit``):
            N/A

        results (:obj:`PollResults <stdgram.raw.base.PollResults>`):
            N/A

        peer (:obj:`Peer <stdgram.raw.base.Peer>`, *optional*):
            N/A

        msg_id (``int`` ``32-bit``, *optional*):
            N/A

        top_msg_id (``int`` ``32-bit``, *optional*):
            N/A

        poll (:obj:`Poll <stdgram.raw.base.Poll>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["poll_id", "results", "peer", "msg_id", "top_msg_id", "poll"]

    ID = 0xd64c522b
    QUALNAME = "types.UpdateMessagePoll"

    def __init__(self, *, poll_id: int, results: raw.base.PollResults, peer: raw.base.Peer | None = None, msg_id: int | None = None, top_msg_id: int | None = None, poll: raw.base.Poll | None = None) -> None:
        self.poll_id = poll_id  # long
        self.results = results  # PollResults
        self.peer = peer  # flags.1?Peer
        self.msg_id = msg_id  # flags.1?int
        self.top_msg_id = top_msg_id  # flags.2?int
        self.poll = poll  # flags.0?Poll

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateMessagePoll:
        
        flags = Int.read(b)
        
        peer = TLObject.read(b) if flags & (1 << 1) else None
        
        msg_id = Int.read(b) if flags & (1 << 1) else None
        top_msg_id = Int.read(b) if flags & (1 << 2) else None
        poll_id = Long.read(b)
        
        poll = TLObject.read(b) if flags & (1 << 0) else None
        
        results = TLObject.read(b)
        
        return UpdateMessagePoll(poll_id=poll_id, results=results, peer=peer, msg_id=msg_id, top_msg_id=top_msg_id, poll=poll)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.peer is not None else 0
        flags |= (1 << 1) if self.msg_id is not None else 0
        flags |= (1 << 2) if self.top_msg_id is not None else 0
        flags |= (1 << 0) if self.poll is not None else 0
        b.write(Int(flags))
        
        if self.peer is not None:
            b.write(self.peer.write())
        
        if self.msg_id is not None:
            b.write(Int(self.msg_id))
        
        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))
        
        b.write(Long(self.poll_id))
        
        if self.poll is not None:
            b.write(self.poll.write())
        
        b.write(self.results.write())
        
        return b.getvalue()
