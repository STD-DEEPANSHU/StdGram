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


class UpdateServiceNotification(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.Update`.

    Details:
        - Layer: ``229``
        - ID: ``EBE46819``

    Parameters:
        type (``str``):
            N/A

        message (``str``):
            N/A

        media (:obj:`MessageMedia <stdgram.raw.base.MessageMedia>`):
            N/A

        entities (List of :obj:`MessageEntity <stdgram.raw.base.MessageEntity>`):
            N/A

        popup (``bool``, *optional*):
            N/A

        invert_media (``bool``, *optional*):
            N/A

        inbox_date (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: list[str] = ["type", "message", "media", "entities", "popup", "invert_media", "inbox_date"]

    ID = 0xebe46819
    QUALNAME = "types.UpdateServiceNotification"

    def __init__(self, *, type: str, message: str, media: raw.base.MessageMedia, entities: list[raw.base.MessageEntity], popup: bool | None = None, invert_media: bool | None = None, inbox_date: int | None = None) -> None:
        self.type = type  # string
        self.message = message  # string
        self.media = media  # MessageMedia
        self.entities = entities  # Vector<MessageEntity>
        self.popup = popup  # flags.0?true
        self.invert_media = invert_media  # flags.2?true
        self.inbox_date = inbox_date  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateServiceNotification:
        
        flags = Int.read(b)
        
        popup = True if flags & (1 << 0) else False
        invert_media = True if flags & (1 << 2) else False
        inbox_date = Int.read(b) if flags & (1 << 1) else None
        type = String.read(b)
        
        message = String.read(b)
        
        media = TLObject.read(b)
        
        entities = TLObject.read(b)
        
        return UpdateServiceNotification(type=type, message=message, media=media, entities=entities, popup=popup, invert_media=invert_media, inbox_date=inbox_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.popup else 0
        flags |= (1 << 2) if self.invert_media else 0
        flags |= (1 << 1) if self.inbox_date is not None else 0
        b.write(Int(flags))
        
        if self.inbox_date is not None:
            b.write(Int(self.inbox_date))
        
        b.write(String(self.type))
        
        b.write(String(self.message))
        
        b.write(self.media.write())
        
        b.write(Vector(self.entities))
        
        return b.getvalue()
