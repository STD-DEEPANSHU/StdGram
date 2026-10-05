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


class InputReplyToMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputReplyTo`.

    Details:
        - Layer: ``229``
        - ID: ``3BD4B7C2``

    Parameters:
        reply_to_msg_id (``int`` ``32-bit``):
            N/A

        top_msg_id (``int`` ``32-bit``, *optional*):
            N/A

        reply_to_peer_id (:obj:`InputPeer <stdgram.raw.base.InputPeer>`, *optional*):
            N/A

        quote_text (``str``, *optional*):
            N/A

        quote_entities (List of :obj:`MessageEntity <stdgram.raw.base.MessageEntity>`, *optional*):
            N/A

        quote_offset (``int`` ``32-bit``, *optional*):
            N/A

        monoforum_peer_id (:obj:`InputPeer <stdgram.raw.base.InputPeer>`, *optional*):
            N/A

        todo_item_id (``int`` ``32-bit``, *optional*):
            N/A

        poll_option (``bytes``, *optional*):
            N/A

    """

    __slots__: list[str] = ["reply_to_msg_id", "top_msg_id", "reply_to_peer_id", "quote_text", "quote_entities", "quote_offset", "monoforum_peer_id", "todo_item_id", "poll_option"]

    ID = 0x3bd4b7c2
    QUALNAME = "types.InputReplyToMessage"

    def __init__(self, *, reply_to_msg_id: int, top_msg_id: int | None = None, reply_to_peer_id: raw.base.InputPeer | None = None, quote_text: str | None = None, quote_entities: list[raw.base.MessageEntity] | None = None, quote_offset: int | None = None, monoforum_peer_id: raw.base.InputPeer | None = None, todo_item_id: int | None = None, poll_option: bytes | None = None) -> None:
        self.reply_to_msg_id = reply_to_msg_id  # int
        self.top_msg_id = top_msg_id  # flags.0?int
        self.reply_to_peer_id = reply_to_peer_id  # flags.1?InputPeer
        self.quote_text = quote_text  # flags.2?string
        self.quote_entities = quote_entities  # flags.3?Vector<MessageEntity>
        self.quote_offset = quote_offset  # flags.4?int
        self.monoforum_peer_id = monoforum_peer_id  # flags.5?InputPeer
        self.todo_item_id = todo_item_id  # flags.6?int
        self.poll_option = poll_option  # flags.7?bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputReplyToMessage:
        
        flags = Int.read(b)
        
        reply_to_msg_id = Int.read(b)
        
        top_msg_id = Int.read(b) if flags & (1 << 0) else None
        reply_to_peer_id = TLObject.read(b) if flags & (1 << 1) else None
        
        quote_text = String.read(b) if flags & (1 << 2) else None
        quote_entities = TLObject.read(b) if flags & (1 << 3) else []
        
        quote_offset = Int.read(b) if flags & (1 << 4) else None
        monoforum_peer_id = TLObject.read(b) if flags & (1 << 5) else None
        
        todo_item_id = Int.read(b) if flags & (1 << 6) else None
        poll_option = Bytes.read(b) if flags & (1 << 7) else None
        return InputReplyToMessage(reply_to_msg_id=reply_to_msg_id, top_msg_id=top_msg_id, reply_to_peer_id=reply_to_peer_id, quote_text=quote_text, quote_entities=quote_entities, quote_offset=quote_offset, monoforum_peer_id=monoforum_peer_id, todo_item_id=todo_item_id, poll_option=poll_option)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.top_msg_id is not None else 0
        flags |= (1 << 1) if self.reply_to_peer_id is not None else 0
        flags |= (1 << 2) if self.quote_text is not None else 0
        flags |= (1 << 3) if self.quote_entities else 0
        flags |= (1 << 4) if self.quote_offset is not None else 0
        flags |= (1 << 5) if self.monoforum_peer_id is not None else 0
        flags |= (1 << 6) if self.todo_item_id is not None else 0
        flags |= (1 << 7) if self.poll_option is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.reply_to_msg_id))
        
        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))
        
        if self.reply_to_peer_id is not None:
            b.write(self.reply_to_peer_id.write())
        
        if self.quote_text is not None:
            b.write(String(self.quote_text))
        
        if self.quote_entities is not None:
            b.write(Vector(self.quote_entities))
        
        if self.quote_offset is not None:
            b.write(Int(self.quote_offset))
        
        if self.monoforum_peer_id is not None:
            b.write(self.monoforum_peer_id.write())
        
        if self.todo_item_id is not None:
            b.write(Int(self.todo_item_id))
        
        if self.poll_option is not None:
            b.write(Bytes(self.poll_option))
        
        return b.getvalue()
