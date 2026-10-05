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


class SendMessage(TLObject["raw.base.Updates"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``BA8D5F35``

    Parameters:
        receiver_id (:obj:`InputUser <stdgram.raw.base.InputUser>`):
            N/A

        message (``str``):
            N/A

        random_id (``int`` ``64-bit``):
            N/A

        invert_media (``bool``, *optional*):
            N/A

        welcome (``bool``, *optional*):
            N/A

        anchor (``bool``, *optional*):
            N/A

        noforwards (``bool``, *optional*):
            N/A

        peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`, *optional*):
            N/A

        query_id (``int`` ``64-bit``, *optional*):
            N/A

        entities (List of :obj:`MessageEntity <stdgram.raw.base.MessageEntity>`, *optional*):
            N/A

        media (:obj:`InputMedia <stdgram.raw.base.InputMedia>`, *optional*):
            N/A

        reply_markup (:obj:`ReplyMarkup <stdgram.raw.base.ReplyMarkup>`, *optional*):
            N/A

        rich_message (:obj:`InputRichMessage <stdgram.raw.base.InputRichMessage>`, *optional*):
            N/A

        reply_to (:obj:`InputReplyTo <stdgram.raw.base.InputReplyTo>`, *optional*):
            N/A

    Returns:
        :obj:`Updates <stdgram.raw.base.Updates>`
    """

    __slots__: list[str] = ["receiver_id", "message", "random_id", "invert_media", "welcome", "anchor", "noforwards", "peer", "query_id", "entities", "media", "reply_markup", "rich_message", "reply_to"]

    ID = 0xba8d5f35
    QUALNAME = "functions.ephemeral.SendMessage"

    def __init__(self, *, receiver_id: raw.base.InputUser, message: str, random_id: int, invert_media: bool | None = None, welcome: bool | None = None, anchor: bool | None = None, noforwards: bool | None = None, peer: raw.base.InputPeer | None = None, query_id: int | None = None, entities: list[raw.base.MessageEntity] | None = None, media: raw.base.InputMedia | None = None, reply_markup: raw.base.ReplyMarkup | None = None, rich_message: raw.base.InputRichMessage | None = None, reply_to: raw.base.InputReplyTo | None = None) -> None:
        self.receiver_id = receiver_id  # InputUser
        self.message = message  # string
        self.random_id = random_id  # long
        self.invert_media = invert_media  # flags.6?true
        self.welcome = welcome  # flags.7?true
        self.anchor = anchor  # flags.9?true
        self.noforwards = noforwards  # flags.10?true
        self.peer = peer  # flags.8?InputPeer
        self.query_id = query_id  # flags.0?long
        self.entities = entities  # flags.1?Vector<MessageEntity>
        self.media = media  # flags.2?InputMedia
        self.reply_markup = reply_markup  # flags.3?ReplyMarkup
        self.rich_message = rich_message  # flags.4?InputRichMessage
        self.reply_to = reply_to  # flags.5?InputReplyTo

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SendMessage:
        
        flags = Int.read(b)
        
        invert_media = True if flags & (1 << 6) else False
        welcome = True if flags & (1 << 7) else False
        anchor = True if flags & (1 << 9) else False
        noforwards = True if flags & (1 << 10) else False
        peer = TLObject.read(b) if flags & (1 << 8) else None
        
        receiver_id = TLObject.read(b)
        
        query_id = Long.read(b) if flags & (1 << 0) else None
        message = String.read(b)
        
        entities = TLObject.read(b) if flags & (1 << 1) else []
        
        media = TLObject.read(b) if flags & (1 << 2) else None
        
        reply_markup = TLObject.read(b) if flags & (1 << 3) else None
        
        rich_message = TLObject.read(b) if flags & (1 << 4) else None
        
        random_id = Long.read(b)
        
        reply_to = TLObject.read(b) if flags & (1 << 5) else None
        
        return SendMessage(receiver_id=receiver_id, message=message, random_id=random_id, invert_media=invert_media, welcome=welcome, anchor=anchor, noforwards=noforwards, peer=peer, query_id=query_id, entities=entities, media=media, reply_markup=reply_markup, rich_message=rich_message, reply_to=reply_to)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 6) if self.invert_media else 0
        flags |= (1 << 7) if self.welcome else 0
        flags |= (1 << 9) if self.anchor else 0
        flags |= (1 << 10) if self.noforwards else 0
        flags |= (1 << 8) if self.peer is not None else 0
        flags |= (1 << 0) if self.query_id is not None else 0
        flags |= (1 << 1) if self.entities else 0
        flags |= (1 << 2) if self.media is not None else 0
        flags |= (1 << 3) if self.reply_markup is not None else 0
        flags |= (1 << 4) if self.rich_message is not None else 0
        flags |= (1 << 5) if self.reply_to is not None else 0
        b.write(Int(flags))
        
        if self.peer is not None:
            b.write(self.peer.write())
        
        b.write(self.receiver_id.write())
        
        if self.query_id is not None:
            b.write(Long(self.query_id))
        
        b.write(String(self.message))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.media is not None:
            b.write(self.media.write())
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        if self.rich_message is not None:
            b.write(self.rich_message.write())
        
        b.write(Long(self.random_id))
        
        if self.reply_to is not None:
            b.write(self.reply_to.write())
        
        return b.getvalue()
