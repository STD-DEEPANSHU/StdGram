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


class GetRecentStickers(TLObject["raw.base.messages.RecentStickers"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``9DA9403B``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

        attached (``bool``, *optional*):
            N/A

    Returns:
        :obj:`messages.RecentStickers <stdgram.raw.base.messages.RecentStickers>`
    """

    __slots__: list[str] = ["hash", "attached"]

    ID = 0x9da9403b
    QUALNAME = "functions.messages.GetRecentStickers"

    def __init__(self, *, hash: int, attached: bool | None = None) -> None:
        self.hash = hash  # long
        self.attached = attached  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GetRecentStickers:
        
        flags = Int.read(b)
        
        attached = True if flags & (1 << 0) else False
        hash = Long.read(b)
        
        return GetRecentStickers(hash=hash, attached=attached)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.attached else 0
        b.write(Int(flags))
        
        b.write(Long(self.hash))
        
        return b.getvalue()
