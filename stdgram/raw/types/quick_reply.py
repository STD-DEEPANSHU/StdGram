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


class QuickReply(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.QuickReply`.

    Details:
        - Layer: ``229``
        - ID: ``697102B``

    Parameters:
        shortcut_id (``int`` ``32-bit``):
            N/A

        shortcut (``str``):
            N/A

        top_message (``int`` ``32-bit``):
            N/A

        count (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["shortcut_id", "shortcut", "top_message", "count"]

    ID = 0x697102b
    QUALNAME = "types.QuickReply"

    def __init__(self, *, shortcut_id: int, shortcut: str, top_message: int, count: int) -> None:
        self.shortcut_id = shortcut_id  # int
        self.shortcut = shortcut  # string
        self.top_message = top_message  # int
        self.count = count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> QuickReply:
        # No flags
        
        shortcut_id = Int.read(b)
        
        shortcut = String.read(b)
        
        top_message = Int.read(b)
        
        count = Int.read(b)
        
        return QuickReply(shortcut_id=shortcut_id, shortcut=shortcut, top_message=top_message, count=count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.shortcut_id))
        
        b.write(String(self.shortcut))
        
        b.write(Int(self.top_message))
        
        b.write(Int(self.count))
        
        return b.getvalue()
