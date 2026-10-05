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


class EditInlineBotMessage(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``A423BB51``

    Parameters:
        id (:obj:`InputBotInlineMessageID <stdgram.raw.base.InputBotInlineMessageID>`):
            N/A

        no_webpage (``bool``, *optional*):
            N/A

        invert_media (``bool``, *optional*):
            N/A

        message (``str``, *optional*):
            N/A

        media (:obj:`InputMedia <stdgram.raw.base.InputMedia>`, *optional*):
            N/A

        reply_markup (:obj:`ReplyMarkup <stdgram.raw.base.ReplyMarkup>`, *optional*):
            N/A

        entities (List of :obj:`MessageEntity <stdgram.raw.base.MessageEntity>`, *optional*):
            N/A

        rich_message (:obj:`InputRichMessage <stdgram.raw.base.InputRichMessage>`, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["id", "no_webpage", "invert_media", "message", "media", "reply_markup", "entities", "rich_message"]

    ID = 0xa423bb51
    QUALNAME = "functions.messages.EditInlineBotMessage"

    def __init__(self, *, id: raw.base.InputBotInlineMessageID, no_webpage: bool | None = None, invert_media: bool | None = None, message: str | None = None, media: raw.base.InputMedia | None = None, reply_markup: raw.base.ReplyMarkup | None = None, entities: list[raw.base.MessageEntity] | None = None, rich_message: raw.base.InputRichMessage | None = None) -> None:
        self.id = id  # InputBotInlineMessageID
        self.no_webpage = no_webpage  # flags.1?true
        self.invert_media = invert_media  # flags.16?true
        self.message = message  # flags.11?string
        self.media = media  # flags.14?InputMedia
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup
        self.entities = entities  # flags.3?Vector<MessageEntity>
        self.rich_message = rich_message  # flags.23?InputRichMessage

    @staticmethod
    def read(b: BytesIO, *args: Any) -> EditInlineBotMessage:
        
        flags = Int.read(b)
        
        no_webpage = True if flags & (1 << 1) else False
        invert_media = True if flags & (1 << 16) else False
        id = TLObject.read(b)
        
        message = String.read(b) if flags & (1 << 11) else None
        media = TLObject.read(b) if flags & (1 << 14) else None
        
        reply_markup = TLObject.read(b) if flags & (1 << 2) else None
        
        entities = TLObject.read(b) if flags & (1 << 3) else []
        
        rich_message = TLObject.read(b) if flags & (1 << 23) else None
        
        return EditInlineBotMessage(id=id, no_webpage=no_webpage, invert_media=invert_media, message=message, media=media, reply_markup=reply_markup, entities=entities, rich_message=rich_message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.no_webpage else 0
        flags |= (1 << 16) if self.invert_media else 0
        flags |= (1 << 11) if self.message is not None else 0
        flags |= (1 << 14) if self.media is not None else 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        flags |= (1 << 3) if self.entities else 0
        flags |= (1 << 23) if self.rich_message is not None else 0
        b.write(Int(flags))
        
        b.write(self.id.write())
        
        if self.message is not None:
            b.write(String(self.message))
        
        if self.media is not None:
            b.write(self.media.write())
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.rich_message is not None:
            b.write(self.rich_message.write())
        
        return b.getvalue()
