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


class SendPaidReaction(TLObject["raw.base.Updates"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``58BBCB50``

    Parameters:
        peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        msg_id (``int`` ``32-bit``):
            N/A

        count (``int`` ``32-bit``):
            N/A

        random_id (``int`` ``64-bit``):
            N/A

        private (:obj:`PaidReactionPrivacy <stdgram.raw.base.PaidReactionPrivacy>`, *optional*):
            N/A

    Returns:
        :obj:`Updates <stdgram.raw.base.Updates>`
    """

    __slots__: list[str] = ["peer", "msg_id", "count", "random_id", "private"]

    ID = 0x58bbcb50
    QUALNAME = "functions.messages.SendPaidReaction"

    def __init__(self, *, peer: raw.base.InputPeer, msg_id: int, count: int, random_id: int, private: raw.base.PaidReactionPrivacy | None = None) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int
        self.count = count  # int
        self.random_id = random_id  # long
        self.private = private  # flags.0?PaidReactionPrivacy

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SendPaidReaction:
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        count = Int.read(b)
        
        random_id = Long.read(b)
        
        private = TLObject.read(b) if flags & (1 << 0) else None
        
        return SendPaidReaction(peer=peer, msg_id=msg_id, count=count, random_id=random_id, private=private)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.private is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(Int(self.count))
        
        b.write(Long(self.random_id))
        
        if self.private is not None:
            b.write(self.private.write())
        
        return b.getvalue()
