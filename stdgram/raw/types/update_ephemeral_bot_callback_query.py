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


class UpdateEphemeralBotCallbackQuery(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.Update`.

    Details:
        - Layer: ``229``
        - ID: ``7C1079D6``

    Parameters:
        query_id (``int`` ``64-bit``):
            N/A

        user_id (``int`` ``64-bit``):
            N/A

        msg_id (``int`` ``32-bit``):
            N/A

        data (``bytes``):
            N/A

        message (:obj:`EphemeralMessage <stdgram.raw.base.EphemeralMessage>`):
            N/A

        peer (:obj:`Peer <stdgram.raw.base.Peer>`, *optional*):
            N/A

        chat_instance (``int`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: list[str] = ["query_id", "user_id", "msg_id", "data", "message", "peer", "chat_instance"]

    ID = 0x7c1079d6
    QUALNAME = "types.UpdateEphemeralBotCallbackQuery"

    def __init__(self, *, query_id: int, user_id: int, msg_id: int, data: bytes, message: raw.base.EphemeralMessage, peer: raw.base.Peer | None = None, chat_instance: int | None = None) -> None:
        self.query_id = query_id  # long
        self.user_id = user_id  # long
        self.msg_id = msg_id  # int
        self.data = data  # bytes
        self.message = message  # EphemeralMessage
        self.peer = peer  # flags.0?Peer
        self.chat_instance = chat_instance  # flags.1?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateEphemeralBotCallbackQuery:
        
        flags = Int.read(b)
        
        query_id = Long.read(b)
        
        user_id = Long.read(b)
        
        peer = TLObject.read(b) if flags & (1 << 0) else None
        
        msg_id = Int.read(b)
        
        data = Bytes.read(b)
        
        chat_instance = Long.read(b) if flags & (1 << 1) else None
        message = TLObject.read(b)
        
        return UpdateEphemeralBotCallbackQuery(query_id=query_id, user_id=user_id, msg_id=msg_id, data=data, message=message, peer=peer, chat_instance=chat_instance)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.peer is not None else 0
        flags |= (1 << 1) if self.chat_instance is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.query_id))
        
        b.write(Long(self.user_id))
        
        if self.peer is not None:
            b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(Bytes(self.data))
        
        if self.chat_instance is not None:
            b.write(Long(self.chat_instance))
        
        b.write(self.message.write())
        
        return b.getvalue()
