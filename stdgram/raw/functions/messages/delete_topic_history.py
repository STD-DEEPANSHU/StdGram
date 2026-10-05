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


class DeleteTopicHistory(TLObject["raw.base.messages.AffectedHistory"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``D2816F10``

    Parameters:
        peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        top_msg_id (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`messages.AffectedHistory <stdgram.raw.base.messages.AffectedHistory>`
    """

    __slots__: list[str] = ["peer", "top_msg_id"]

    ID = 0xd2816f10
    QUALNAME = "functions.messages.DeleteTopicHistory"

    def __init__(self, *, peer: raw.base.InputPeer, top_msg_id: int) -> None:
        self.peer = peer  # InputPeer
        self.top_msg_id = top_msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> DeleteTopicHistory:
        # No flags
        
        peer = TLObject.read(b)
        
        top_msg_id = Int.read(b)
        
        return DeleteTopicHistory(peer=peer, top_msg_id=top_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.top_msg_id))
        
        return b.getvalue()
