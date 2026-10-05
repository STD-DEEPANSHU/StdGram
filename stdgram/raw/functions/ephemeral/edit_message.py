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


class EditMessage(TLObject["raw.base.Updates"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``CF9C725B``

    Parameters:
        receiver_id (:obj:`InputUser <stdgram.raw.base.InputUser>`):
            N/A

        id (``int`` ``32-bit``):
            N/A

        invert_media (``bool``, *optional*):
            N/A

        welcome (``bool``, *optional*):
            N/A

        peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`, *optional*):
            N/A

        message (``str``, *optional*):
            N/A

        media (:obj:`InputMedia <stdgram.raw.base.InputMedia>`, *optional*):
            N/A

        entities (List of :obj:`MessageEntity <stdgram.raw.base.MessageEntity>`, *optional*):
            N/A

        reply_markup (:obj:`ReplyMarkup <stdgram.raw.base.ReplyMarkup>`, *optional*):
            N/A

        rich_message (:obj:`InputRichMessage <stdgram.raw.base.InputRichMessage>`, *optional*):
            N/A

    Returns:
        :obj:`Updates <stdgram.raw.base.Updates>`
    """

    __slots__: list[str] = ["receiver_id", "id", "invert_media", "welcome", "peer", "message", "media", "entities", "reply_markup", "rich_message"]

    ID = 0xcf9c725b
    QUALNAME = "functions.ephemeral.EditMessage"

    def __init__(self, *, receiver_id: raw.base.InputUser, id: int, invert_media: bool | None = None, welcome: bool | None = None, peer: raw.base.InputPeer | None = None, message: str | None = None, media: raw.base.InputMedia | None = None, entities: list[raw.base.MessageEntity] | None = None, reply_markup: raw.base.ReplyMarkup | None = None, rich_message: raw.base.InputRichMessage | None = None) -> None:
        self.receiver_id = receiver_id  # InputUser
        self.id = id  # int
        self.invert_media = invert_media  # flags.5?true
        self.welcome = welcome  # flags.6?true
        self.peer = peer  # flags.7?InputPeer
        self.message = message  # flags.0?string
        self.media = media  # flags.3?InputMedia
        self.entities = entities  # flags.1?Vector<MessageEntity>
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup
        self.rich_message = rich_message  # flags.4?InputRichMessage

    @staticmethod
    def read(b: BytesIO, *args: Any) -> EditMessage:
        
        flags = Int.read(b)
        
        invert_media = True if flags & (1 << 5) else False
        welcome = True if flags & (1 << 6) else False
        peer = TLObject.read(b) if flags & (1 << 7) else None
        
        receiver_id = TLObject.read(b)
        
        id = Int.read(b)
        
        message = String.read(b) if flags & (1 << 0) else None
        media = TLObject.read(b) if flags & (1 << 3) else None
        
        entities = TLObject.read(b) if flags & (1 << 1) else []
        
        reply_markup = TLObject.read(b) if flags & (1 << 2) else None
        
        rich_message = TLObject.read(b) if flags & (1 << 4) else None
        
        return EditMessage(receiver_id=receiver_id, id=id, invert_media=invert_media, welcome=welcome, peer=peer, message=message, media=media, entities=entities, reply_markup=reply_markup, rich_message=rich_message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.invert_media else 0
        flags |= (1 << 6) if self.welcome else 0
        flags |= (1 << 7) if self.peer is not None else 0
        flags |= (1 << 0) if self.message is not None else 0
        flags |= (1 << 3) if self.media is not None else 0
        flags |= (1 << 1) if self.entities else 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        flags |= (1 << 4) if self.rich_message is not None else 0
        b.write(Int(flags))
        
        if self.peer is not None:
            b.write(self.peer.write())
        
        b.write(self.receiver_id.write())
        
        b.write(Int(self.id))
        
        if self.message is not None:
            b.write(String(self.message))
        
        if self.media is not None:
            b.write(self.media.write())
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        if self.rich_message is not None:
            b.write(self.rich_message.write())
        
        return b.getvalue()
