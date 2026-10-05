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


class SetStickerSetThumb(TLObject["raw.base.messages.StickerSet"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``A76A5392``

    Parameters:
        stickerset (:obj:`InputStickerSet <stdgram.raw.base.InputStickerSet>`):
            N/A

        thumb (:obj:`InputDocument <stdgram.raw.base.InputDocument>`, *optional*):
            N/A

        thumb_document_id (``int`` ``64-bit``, *optional*):
            N/A

    Returns:
        :obj:`messages.StickerSet <stdgram.raw.base.messages.StickerSet>`
    """

    __slots__: list[str] = ["stickerset", "thumb", "thumb_document_id"]

    ID = 0xa76a5392
    QUALNAME = "functions.stickers.SetStickerSetThumb"

    def __init__(self, *, stickerset: raw.base.InputStickerSet, thumb: raw.base.InputDocument | None = None, thumb_document_id: int | None = None) -> None:
        self.stickerset = stickerset  # InputStickerSet
        self.thumb = thumb  # flags.0?InputDocument
        self.thumb_document_id = thumb_document_id  # flags.1?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SetStickerSetThumb:
        
        flags = Int.read(b)
        
        stickerset = TLObject.read(b)
        
        thumb = TLObject.read(b) if flags & (1 << 0) else None
        
        thumb_document_id = Long.read(b) if flags & (1 << 1) else None
        return SetStickerSetThumb(stickerset=stickerset, thumb=thumb, thumb_document_id=thumb_document_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.thumb is not None else 0
        flags |= (1 << 1) if self.thumb_document_id is not None else 0
        b.write(Int(flags))
        
        b.write(self.stickerset.write())
        
        if self.thumb is not None:
            b.write(self.thumb.write())
        
        if self.thumb_document_id is not None:
            b.write(Long(self.thumb_document_id))
        
        return b.getvalue()
