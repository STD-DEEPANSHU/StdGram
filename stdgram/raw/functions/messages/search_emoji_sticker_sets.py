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


class SearchEmojiStickerSets(TLObject["raw.base.messages.FoundStickerSets"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``92B4494C``

    Parameters:
        q (``str``):
            N/A

        hash (``int`` ``64-bit``):
            N/A

        exclude_featured (``bool``, *optional*):
            N/A

    Returns:
        :obj:`messages.FoundStickerSets <stdgram.raw.base.messages.FoundStickerSets>`
    """

    __slots__: list[str] = ["q", "hash", "exclude_featured"]

    ID = 0x92b4494c
    QUALNAME = "functions.messages.SearchEmojiStickerSets"

    def __init__(self, *, q: str, hash: int, exclude_featured: bool | None = None) -> None:
        self.q = q  # string
        self.hash = hash  # long
        self.exclude_featured = exclude_featured  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SearchEmojiStickerSets:
        
        flags = Int.read(b)
        
        exclude_featured = True if flags & (1 << 0) else False
        q = String.read(b)
        
        hash = Long.read(b)
        
        return SearchEmojiStickerSets(q=q, hash=hash, exclude_featured=exclude_featured)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.exclude_featured else 0
        b.write(Int(flags))
        
        b.write(String(self.q))
        
        b.write(Long(self.hash))
        
        return b.getvalue()
