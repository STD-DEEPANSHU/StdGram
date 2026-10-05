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


class VideoSizeStickerMarkup(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.VideoSize`.

    Details:
        - Layer: ``229``
        - ID: ``DA082FE``

    Parameters:
        stickerset (:obj:`InputStickerSet <stdgram.raw.base.InputStickerSet>`):
            N/A

        sticker_id (``int`` ``64-bit``):
            N/A

        background_colors (List of ``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["stickerset", "sticker_id", "background_colors"]

    ID = 0xda082fe
    QUALNAME = "types.VideoSizeStickerMarkup"

    def __init__(self, *, stickerset: raw.base.InputStickerSet, sticker_id: int, background_colors: list[int]) -> None:
        self.stickerset = stickerset  # InputStickerSet
        self.sticker_id = sticker_id  # long
        self.background_colors = background_colors  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> VideoSizeStickerMarkup:
        # No flags
        
        stickerset = TLObject.read(b)
        
        sticker_id = Long.read(b)
        
        background_colors = TLObject.read(b, Int)
        
        return VideoSizeStickerMarkup(stickerset=stickerset, sticker_id=sticker_id, background_colors=background_colors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.stickerset.write())
        
        b.write(Long(self.sticker_id))
        
        b.write(Vector(self.background_colors, Int))
        
        return b.getvalue()
