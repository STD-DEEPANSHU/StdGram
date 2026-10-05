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


class AutoSaveSettings(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.AutoSaveSettings`.

    Details:
        - Layer: ``229``
        - ID: ``C84834CE``

    Parameters:
        photos (``bool``, *optional*):
            N/A

        videos (``bool``, *optional*):
            N/A

        video_max_size (``int`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: list[str] = ["photos", "videos", "video_max_size"]

    ID = 0xc84834ce
    QUALNAME = "types.AutoSaveSettings"

    def __init__(self, *, photos: bool | None = None, videos: bool | None = None, video_max_size: int | None = None) -> None:
        self.photos = photos  # flags.0?true
        self.videos = videos  # flags.1?true
        self.video_max_size = video_max_size  # flags.2?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> AutoSaveSettings:
        
        flags = Int.read(b)
        
        photos = True if flags & (1 << 0) else False
        videos = True if flags & (1 << 1) else False
        video_max_size = Long.read(b) if flags & (1 << 2) else None
        return AutoSaveSettings(photos=photos, videos=videos, video_max_size=video_max_size)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.photos else 0
        flags |= (1 << 1) if self.videos else 0
        flags |= (1 << 2) if self.video_max_size is not None else 0
        b.write(Int(flags))
        
        if self.video_max_size is not None:
            b.write(Long(self.video_max_size))
        
        return b.getvalue()
