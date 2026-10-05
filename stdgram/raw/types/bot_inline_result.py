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


class BotInlineResult(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.BotInlineResult`.

    Details:
        - Layer: ``229``
        - ID: ``11965F3A``

    Parameters:
        id (``str``):
            N/A

        type (``str``):
            N/A

        send_message (:obj:`BotInlineMessage <stdgram.raw.base.BotInlineMessage>`):
            N/A

        title (``str``, *optional*):
            N/A

        description (``str``, *optional*):
            N/A

        url (``str``, *optional*):
            N/A

        thumb (:obj:`WebDocument <stdgram.raw.base.WebDocument>`, *optional*):
            N/A

        content (:obj:`WebDocument <stdgram.raw.base.WebDocument>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["id", "type", "send_message", "title", "description", "url", "thumb", "content"]

    ID = 0x11965f3a
    QUALNAME = "types.BotInlineResult"

    def __init__(self, *, id: str, type: str, send_message: raw.base.BotInlineMessage, title: str | None = None, description: str | None = None, url: str | None = None, thumb: raw.base.WebDocument | None = None, content: raw.base.WebDocument | None = None) -> None:
        self.id = id  # string
        self.type = type  # string
        self.send_message = send_message  # BotInlineMessage
        self.title = title  # flags.1?string
        self.description = description  # flags.2?string
        self.url = url  # flags.3?string
        self.thumb = thumb  # flags.4?WebDocument
        self.content = content  # flags.5?WebDocument

    @staticmethod
    def read(b: BytesIO, *args: Any) -> BotInlineResult:
        
        flags = Int.read(b)
        
        id = String.read(b)
        
        type = String.read(b)
        
        title = String.read(b) if flags & (1 << 1) else None
        description = String.read(b) if flags & (1 << 2) else None
        url = String.read(b) if flags & (1 << 3) else None
        thumb = TLObject.read(b) if flags & (1 << 4) else None
        
        content = TLObject.read(b) if flags & (1 << 5) else None
        
        send_message = TLObject.read(b)
        
        return BotInlineResult(id=id, type=type, send_message=send_message, title=title, description=description, url=url, thumb=thumb, content=content)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.title is not None else 0
        flags |= (1 << 2) if self.description is not None else 0
        flags |= (1 << 3) if self.url is not None else 0
        flags |= (1 << 4) if self.thumb is not None else 0
        flags |= (1 << 5) if self.content is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.id))
        
        b.write(String(self.type))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.description is not None:
            b.write(String(self.description))
        
        if self.url is not None:
            b.write(String(self.url))
        
        if self.thumb is not None:
            b.write(self.thumb.write())
        
        if self.content is not None:
            b.write(self.content.write())
        
        b.write(self.send_message.write())
        
        return b.getvalue()
