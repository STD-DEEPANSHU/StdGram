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


class ReplaceSticker(TLObject["raw.base.messages.StickerSet"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``4696459A``

    Parameters:
        sticker (:obj:`InputDocument <stdgram.raw.base.InputDocument>`):
            N/A

        new_sticker (:obj:`InputStickerSetItem <stdgram.raw.base.InputStickerSetItem>`):
            N/A

    Returns:
        :obj:`messages.StickerSet <stdgram.raw.base.messages.StickerSet>`
    """

    __slots__: list[str] = ["sticker", "new_sticker"]

    ID = 0x4696459a
    QUALNAME = "functions.stickers.ReplaceSticker"

    def __init__(self, *, sticker: raw.base.InputDocument, new_sticker: raw.base.InputStickerSetItem) -> None:
        self.sticker = sticker  # InputDocument
        self.new_sticker = new_sticker  # InputStickerSetItem

    @staticmethod
    def read(b: BytesIO, *args: Any) -> ReplaceSticker:
        # No flags
        
        sticker = TLObject.read(b)
        
        new_sticker = TLObject.read(b)
        
        return ReplaceSticker(sticker=sticker, new_sticker=new_sticker)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.sticker.write())
        
        b.write(self.new_sticker.write())
        
        return b.getvalue()
