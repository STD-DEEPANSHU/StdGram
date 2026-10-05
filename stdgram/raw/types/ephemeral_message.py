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


class EphemeralMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.EphemeralMessage`.

    Details:
        - Layer: ``229``
        - ID: ``DD27BEE9``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        from_id (:obj:`Peer <stdgram.raw.base.Peer>`):
            N/A

        receiver_id (``int`` ``64-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        message (``str``):
            N/A

        out (``bool``, *optional*):
            N/A

        welcome_template (``bool``, *optional*):
            N/A

        invert_media (``bool``, *optional*):
            N/A

        noforwards (``bool``, *optional*):
            N/A

        peer_id (:obj:`Peer <stdgram.raw.base.Peer>`, *optional*):
            N/A

        top_msg_id (``int`` ``32-bit``, *optional*):
            N/A

        entities (List of :obj:`MessageEntity <stdgram.raw.base.MessageEntity>`, *optional*):
            N/A

        media (:obj:`MessageMedia <stdgram.raw.base.MessageMedia>`, *optional*):
            N/A

        reply_markup (:obj:`ReplyMarkup <stdgram.raw.base.ReplyMarkup>`, *optional*):
            N/A

        reply_to (:obj:`MessageReplyHeader <stdgram.raw.base.MessageReplyHeader>`, *optional*):
            N/A

        rich_message (:obj:`RichMessage <stdgram.raw.base.RichMessage>`, *optional*):
            N/A

        chat_instance (``int`` ``64-bit``, *optional*):
            N/A

        anchor_msg_id (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: list[str] = ["id", "from_id", "receiver_id", "date", "message", "out", "welcome_template", "invert_media", "noforwards", "peer_id", "top_msg_id", "entities", "media", "reply_markup", "reply_to", "rich_message", "chat_instance", "anchor_msg_id"]

    ID = 0xdd27bee9
    QUALNAME = "types.EphemeralMessage"

    def __init__(self, *, id: int, from_id: raw.base.Peer, receiver_id: int, date: int, message: str, out: bool | None = None, welcome_template: bool | None = None, invert_media: bool | None = None, noforwards: bool | None = None, peer_id: raw.base.Peer | None = None, top_msg_id: int | None = None, entities: list[raw.base.MessageEntity] | None = None, media: raw.base.MessageMedia | None = None, reply_markup: raw.base.ReplyMarkup | None = None, reply_to: raw.base.MessageReplyHeader | None = None, rich_message: raw.base.RichMessage | None = None, chat_instance: int | None = None, anchor_msg_id: int | None = None) -> None:
        self.id = id  # int
        self.from_id = from_id  # Peer
        self.receiver_id = receiver_id  # long
        self.date = date  # int
        self.message = message  # string
        self.out = out  # flags.0?true
        self.welcome_template = welcome_template  # flags.5?true
        self.invert_media = invert_media  # flags.7?true
        self.noforwards = noforwards  # flags.12?true
        self.peer_id = peer_id  # flags.9?Peer
        self.top_msg_id = top_msg_id  # flags.1?int
        self.entities = entities  # flags.2?Vector<MessageEntity>
        self.media = media  # flags.3?MessageMedia
        self.reply_markup = reply_markup  # flags.4?ReplyMarkup
        self.reply_to = reply_to  # flags.6?MessageReplyHeader
        self.rich_message = rich_message  # flags.8?RichMessage
        self.chat_instance = chat_instance  # flags.10?long
        self.anchor_msg_id = anchor_msg_id  # flags.11?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> EphemeralMessage:
        
        flags = Int.read(b)
        
        out = True if flags & (1 << 0) else False
        welcome_template = True if flags & (1 << 5) else False
        invert_media = True if flags & (1 << 7) else False
        noforwards = True if flags & (1 << 12) else False
        id = Int.read(b)
        
        from_id = TLObject.read(b)
        
        peer_id = TLObject.read(b) if flags & (1 << 9) else None
        
        receiver_id = Long.read(b)
        
        top_msg_id = Int.read(b) if flags & (1 << 1) else None
        date = Int.read(b)
        
        message = String.read(b)
        
        entities = TLObject.read(b) if flags & (1 << 2) else []
        
        media = TLObject.read(b) if flags & (1 << 3) else None
        
        reply_markup = TLObject.read(b) if flags & (1 << 4) else None
        
        reply_to = TLObject.read(b) if flags & (1 << 6) else None
        
        rich_message = TLObject.read(b) if flags & (1 << 8) else None
        
        chat_instance = Long.read(b) if flags & (1 << 10) else None
        anchor_msg_id = Int.read(b) if flags & (1 << 11) else None
        return EphemeralMessage(id=id, from_id=from_id, receiver_id=receiver_id, date=date, message=message, out=out, welcome_template=welcome_template, invert_media=invert_media, noforwards=noforwards, peer_id=peer_id, top_msg_id=top_msg_id, entities=entities, media=media, reply_markup=reply_markup, reply_to=reply_to, rich_message=rich_message, chat_instance=chat_instance, anchor_msg_id=anchor_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.out else 0
        flags |= (1 << 5) if self.welcome_template else 0
        flags |= (1 << 7) if self.invert_media else 0
        flags |= (1 << 12) if self.noforwards else 0
        flags |= (1 << 9) if self.peer_id is not None else 0
        flags |= (1 << 1) if self.top_msg_id is not None else 0
        flags |= (1 << 2) if self.entities else 0
        flags |= (1 << 3) if self.media is not None else 0
        flags |= (1 << 4) if self.reply_markup is not None else 0
        flags |= (1 << 6) if self.reply_to is not None else 0
        flags |= (1 << 8) if self.rich_message is not None else 0
        flags |= (1 << 10) if self.chat_instance is not None else 0
        flags |= (1 << 11) if self.anchor_msg_id is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(self.from_id.write())
        
        if self.peer_id is not None:
            b.write(self.peer_id.write())
        
        b.write(Long(self.receiver_id))
        
        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))
        
        b.write(Int(self.date))
        
        b.write(String(self.message))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.media is not None:
            b.write(self.media.write())
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        if self.reply_to is not None:
            b.write(self.reply_to.write())
        
        if self.rich_message is not None:
            b.write(self.rich_message.write())
        
        if self.chat_instance is not None:
            b.write(Long(self.chat_instance))
        
        if self.anchor_msg_id is not None:
            b.write(Int(self.anchor_msg_id))
        
        return b.getvalue()
