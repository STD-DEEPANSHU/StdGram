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


class PageBlockEmbedPost(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.PageBlock`.

    Details:
        - Layer: ``229``
        - ID: ``F259A80B``

    Parameters:
        url (``str``):
            N/A

        webpage_id (``int`` ``64-bit``):
            N/A

        author_photo_id (``int`` ``64-bit``):
            N/A

        author (``str``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        blocks (List of :obj:`PageBlock <stdgram.raw.base.PageBlock>`):
            N/A

        caption (:obj:`PageCaption <stdgram.raw.base.PageCaption>`):
            N/A

    """

    __slots__: list[str] = ["url", "webpage_id", "author_photo_id", "author", "date", "blocks", "caption"]

    ID = 0xf259a80b
    QUALNAME = "types.PageBlockEmbedPost"

    def __init__(self, *, url: str, webpage_id: int, author_photo_id: int, author: str, date: int, blocks: list[raw.base.PageBlock], caption: raw.base.PageCaption) -> None:
        self.url = url  # string
        self.webpage_id = webpage_id  # long
        self.author_photo_id = author_photo_id  # long
        self.author = author  # string
        self.date = date  # int
        self.blocks = blocks  # Vector<PageBlock>
        self.caption = caption  # PageCaption

    @staticmethod
    def read(b: BytesIO, *args: Any) -> PageBlockEmbedPost:
        # No flags
        
        url = String.read(b)
        
        webpage_id = Long.read(b)
        
        author_photo_id = Long.read(b)
        
        author = String.read(b)
        
        date = Int.read(b)
        
        blocks = TLObject.read(b)
        
        caption = TLObject.read(b)
        
        return PageBlockEmbedPost(url=url, webpage_id=webpage_id, author_photo_id=author_photo_id, author=author, date=date, blocks=blocks, caption=caption)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        b.write(Long(self.webpage_id))
        
        b.write(Long(self.author_photo_id))
        
        b.write(String(self.author))
        
        b.write(Int(self.date))
        
        b.write(Vector(self.blocks))
        
        b.write(self.caption.write())
        
        return b.getvalue()
