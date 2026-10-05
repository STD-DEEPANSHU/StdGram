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


class UpdateBotDeleteBusinessMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.Update`.

    Details:
        - Layer: ``229``
        - ID: ``A02A982E``

    Parameters:
        connection_id (``str``):
            N/A

        peer (:obj:`Peer <stdgram.raw.base.Peer>`):
            N/A

        messages (List of ``int`` ``32-bit``):
            N/A

        qts (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["connection_id", "peer", "messages", "qts"]

    ID = 0xa02a982e
    QUALNAME = "types.UpdateBotDeleteBusinessMessage"

    def __init__(self, *, connection_id: str, peer: raw.base.Peer, messages: list[int], qts: int) -> None:
        self.connection_id = connection_id  # string
        self.peer = peer  # Peer
        self.messages = messages  # Vector<int>
        self.qts = qts  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateBotDeleteBusinessMessage:
        # No flags
        
        connection_id = String.read(b)
        
        peer = TLObject.read(b)
        
        messages = TLObject.read(b, Int)
        
        qts = Int.read(b)
        
        return UpdateBotDeleteBusinessMessage(connection_id=connection_id, peer=peer, messages=messages, qts=qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.connection_id))
        
        b.write(self.peer.write())
        
        b.write(Vector(self.messages, Int))
        
        b.write(Int(self.qts))
        
        return b.getvalue()
