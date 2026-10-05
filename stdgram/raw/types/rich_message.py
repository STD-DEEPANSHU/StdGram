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


class RichMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.RichMessage`.

    Details:
        - Layer: ``229``
        - ID: ``BAF39D8B``

    Parameters:
        blocks (List of :obj:`PageBlock <stdgram.raw.base.PageBlock>`):
            N/A

        photos (List of :obj:`Photo <stdgram.raw.base.Photo>`):
            N/A

        documents (List of :obj:`Document <stdgram.raw.base.Document>`):
            N/A

        rtl (``bool``, *optional*):
            N/A

        part (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["blocks", "photos", "documents", "rtl", "part"]

    ID = 0xbaf39d8b
    QUALNAME = "types.RichMessage"

    def __init__(self, *, blocks: list[raw.base.PageBlock], photos: list[raw.base.Photo], documents: list[raw.base.Document], rtl: bool | None = None, part: bool | None = None) -> None:
        self.blocks = blocks  # Vector<PageBlock>
        self.photos = photos  # Vector<Photo>
        self.documents = documents  # Vector<Document>
        self.rtl = rtl  # flags.0?true
        self.part = part  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> RichMessage:
        
        flags = Int.read(b)
        
        rtl = True if flags & (1 << 0) else False
        part = True if flags & (1 << 1) else False
        blocks = TLObject.read(b)
        
        photos = TLObject.read(b)
        
        documents = TLObject.read(b)
        
        return RichMessage(blocks=blocks, photos=photos, documents=documents, rtl=rtl, part=part)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.rtl else 0
        flags |= (1 << 1) if self.part else 0
        b.write(Int(flags))
        
        b.write(Vector(self.blocks))
        
        b.write(Vector(self.photos))
        
        b.write(Vector(self.documents))
        
        return b.getvalue()
