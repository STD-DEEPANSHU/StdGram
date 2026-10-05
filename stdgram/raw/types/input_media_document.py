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


class InputMediaDocument(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputMedia`.

    Details:
        - Layer: ``229``
        - ID: ``A8763AB5``

    Parameters:
        id (:obj:`InputDocument <stdgram.raw.base.InputDocument>`):
            N/A

        spoiler (``bool``, *optional*):
            N/A

        video_cover (:obj:`InputPhoto <stdgram.raw.base.InputPhoto>`, *optional*):
            N/A

        video_timestamp (``int`` ``32-bit``, *optional*):
            N/A

        ttl_seconds (``int`` ``32-bit``, *optional*):
            N/A

        query (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["id", "spoiler", "video_cover", "video_timestamp", "ttl_seconds", "query"]

    ID = 0xa8763ab5
    QUALNAME = "types.InputMediaDocument"

    def __init__(self, *, id: raw.base.InputDocument, spoiler: bool | None = None, video_cover: raw.base.InputPhoto | None = None, video_timestamp: int | None = None, ttl_seconds: int | None = None, query: str | None = None) -> None:
        self.id = id  # InputDocument
        self.spoiler = spoiler  # flags.2?true
        self.video_cover = video_cover  # flags.3?InputPhoto
        self.video_timestamp = video_timestamp  # flags.4?int
        self.ttl_seconds = ttl_seconds  # flags.0?int
        self.query = query  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputMediaDocument:
        
        flags = Int.read(b)
        
        spoiler = True if flags & (1 << 2) else False
        id = TLObject.read(b)
        
        video_cover = TLObject.read(b) if flags & (1 << 3) else None
        
        video_timestamp = Int.read(b) if flags & (1 << 4) else None
        ttl_seconds = Int.read(b) if flags & (1 << 0) else None
        query = String.read(b) if flags & (1 << 1) else None
        return InputMediaDocument(id=id, spoiler=spoiler, video_cover=video_cover, video_timestamp=video_timestamp, ttl_seconds=ttl_seconds, query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.spoiler else 0
        flags |= (1 << 3) if self.video_cover is not None else 0
        flags |= (1 << 4) if self.video_timestamp is not None else 0
        flags |= (1 << 0) if self.ttl_seconds is not None else 0
        flags |= (1 << 1) if self.query is not None else 0
        b.write(Int(flags))
        
        b.write(self.id.write())
        
        if self.video_cover is not None:
            b.write(self.video_cover.write())
        
        if self.video_timestamp is not None:
            b.write(Int(self.video_timestamp))
        
        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))
        
        if self.query is not None:
            b.write(String(self.query))
        
        return b.getvalue()
