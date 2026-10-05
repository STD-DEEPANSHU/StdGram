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
        - ID: ``B106E66C``

    Parameters:
        peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        id (``int`` ``32-bit``):
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

        schedule_date (``int`` ``32-bit``, *optional*):
            N/A

        schedule_repeat_period (``int`` ``32-bit``, *optional*):
            N/A

        quick_reply_shortcut_id (``int`` ``32-bit``, *optional*):
            N/A

        rich_message (:obj:`InputRichMessage <stdgram.raw.base.InputRichMessage>`, *optional*):
            N/A

    Returns:
        :obj:`Updates <stdgram.raw.base.Updates>`
    """

    __slots__: list[str] = ["peer", "id", "no_webpage", "invert_media", "message", "media", "reply_markup", "entities", "schedule_date", "schedule_repeat_period", "quick_reply_shortcut_id", "rich_message"]

    ID = 0xb106e66c
    QUALNAME = "functions.messages.EditMessage"

    def __init__(self, *, peer: raw.base.InputPeer, id: int, no_webpage: bool | None = None, invert_media: bool | None = None, message: str | None = None, media: raw.base.InputMedia | None = None, reply_markup: raw.base.ReplyMarkup | None = None, entities: list[raw.base.MessageEntity] | None = None, schedule_date: int | None = None, schedule_repeat_period: int | None = None, quick_reply_shortcut_id: int | None = None, rich_message: raw.base.InputRichMessage | None = None) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.no_webpage = no_webpage  # flags.1?true
        self.invert_media = invert_media  # flags.16?true
        self.message = message  # flags.11?string
        self.media = media  # flags.14?InputMedia
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup
        self.entities = entities  # flags.3?Vector<MessageEntity>
        self.schedule_date = schedule_date  # flags.15?int
        self.schedule_repeat_period = schedule_repeat_period  # flags.18?int
        self.quick_reply_shortcut_id = quick_reply_shortcut_id  # flags.17?int
        self.rich_message = rich_message  # flags.23?InputRichMessage

    @staticmethod
    def read(b: BytesIO, *args: Any) -> EditMessage:
        
        flags = Int.read(b)
        
        no_webpage = True if flags & (1 << 1) else False
        invert_media = True if flags & (1 << 16) else False
        peer = TLObject.read(b)
        
        id = Int.read(b)
        
        message = String.read(b) if flags & (1 << 11) else None
        media = TLObject.read(b) if flags & (1 << 14) else None
        
        reply_markup = TLObject.read(b) if flags & (1 << 2) else None
        
        entities = TLObject.read(b) if flags & (1 << 3) else []
        
        schedule_date = Int.read(b) if flags & (1 << 15) else None
        schedule_repeat_period = Int.read(b) if flags & (1 << 18) else None
        quick_reply_shortcut_id = Int.read(b) if flags & (1 << 17) else None
        rich_message = TLObject.read(b) if flags & (1 << 23) else None
        
        return EditMessage(peer=peer, id=id, no_webpage=no_webpage, invert_media=invert_media, message=message, media=media, reply_markup=reply_markup, entities=entities, schedule_date=schedule_date, schedule_repeat_period=schedule_repeat_period, quick_reply_shortcut_id=quick_reply_shortcut_id, rich_message=rich_message)

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
        flags |= (1 << 15) if self.schedule_date is not None else 0
        flags |= (1 << 18) if self.schedule_repeat_period is not None else 0
        flags |= (1 << 17) if self.quick_reply_shortcut_id is not None else 0
        flags |= (1 << 23) if self.rich_message is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        if self.message is not None:
            b.write(String(self.message))
        
        if self.media is not None:
            b.write(self.media.write())
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.schedule_date is not None:
            b.write(Int(self.schedule_date))
        
        if self.schedule_repeat_period is not None:
            b.write(Int(self.schedule_repeat_period))
        
        if self.quick_reply_shortcut_id is not None:
            b.write(Int(self.quick_reply_shortcut_id))
        
        if self.rich_message is not None:
            b.write(self.rich_message.write())
        
        return b.getvalue()
