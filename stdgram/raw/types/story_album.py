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


class StoryAlbum(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.StoryAlbum`.

    Details:
        - Layer: ``229``
        - ID: ``9325705A``

    Parameters:
        album_id (``int`` ``32-bit``):
            N/A

        title (``str``):
            N/A

        icon_photo (:obj:`Photo <stdgram.raw.base.Photo>`, *optional*):
            N/A

        icon_video (:obj:`Document <stdgram.raw.base.Document>`, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.CreateAlbum
            stories.UpdateAlbum
    """

    __slots__: list[str] = ["album_id", "title", "icon_photo", "icon_video"]

    ID = 0x9325705a
    QUALNAME = "types.StoryAlbum"

    def __init__(self, *, album_id: int, title: str, icon_photo: raw.base.Photo | None = None, icon_video: raw.base.Document | None = None) -> None:
        self.album_id = album_id  # int
        self.title = title  # string
        self.icon_photo = icon_photo  # flags.0?Photo
        self.icon_video = icon_video  # flags.1?Document

    @staticmethod
    def read(b: BytesIO, *args: Any) -> StoryAlbum:
        
        flags = Int.read(b)
        
        album_id = Int.read(b)
        
        title = String.read(b)
        
        icon_photo = TLObject.read(b) if flags & (1 << 0) else None
        
        icon_video = TLObject.read(b) if flags & (1 << 1) else None
        
        return StoryAlbum(album_id=album_id, title=title, icon_photo=icon_photo, icon_video=icon_video)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.icon_photo is not None else 0
        flags |= (1 << 1) if self.icon_video is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.album_id))
        
        b.write(String(self.title))
        
        if self.icon_photo is not None:
            b.write(self.icon_photo.write())
        
        if self.icon_video is not None:
            b.write(self.icon_video.write())
        
        return b.getvalue()
