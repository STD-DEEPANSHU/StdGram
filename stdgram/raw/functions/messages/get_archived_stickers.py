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


class GetArchivedStickers(TLObject["raw.base.messages.ArchivedStickers"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``57F17692``

    Parameters:
        offset_id (``int`` ``64-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        masks (``bool``, *optional*):
            N/A

        emojis (``bool``, *optional*):
            N/A

    Returns:
        :obj:`messages.ArchivedStickers <stdgram.raw.base.messages.ArchivedStickers>`
    """

    __slots__: list[str] = ["offset_id", "limit", "masks", "emojis"]

    ID = 0x57f17692
    QUALNAME = "functions.messages.GetArchivedStickers"

    def __init__(self, *, offset_id: int, limit: int, masks: bool | None = None, emojis: bool | None = None) -> None:
        self.offset_id = offset_id  # long
        self.limit = limit  # int
        self.masks = masks  # flags.0?true
        self.emojis = emojis  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GetArchivedStickers:
        
        flags = Int.read(b)
        
        masks = True if flags & (1 << 0) else False
        emojis = True if flags & (1 << 1) else False
        offset_id = Long.read(b)
        
        limit = Int.read(b)
        
        return GetArchivedStickers(offset_id=offset_id, limit=limit, masks=masks, emojis=emojis)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.masks else 0
        flags |= (1 << 1) if self.emojis else 0
        b.write(Int(flags))
        
        b.write(Long(self.offset_id))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
