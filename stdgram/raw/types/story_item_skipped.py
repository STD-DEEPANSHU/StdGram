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


class StoryItemSkipped(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.StoryItem`.

    Details:
        - Layer: ``229``
        - ID: ``FFADC913``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        expire_date (``int`` ``32-bit``):
            N/A

        close_friends (``bool``, *optional*):
            N/A

        live (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["id", "date", "expire_date", "close_friends", "live"]

    ID = 0xffadc913
    QUALNAME = "types.StoryItemSkipped"

    def __init__(self, *, id: int, date: int, expire_date: int, close_friends: bool | None = None, live: bool | None = None) -> None:
        self.id = id  # int
        self.date = date  # int
        self.expire_date = expire_date  # int
        self.close_friends = close_friends  # flags.8?true
        self.live = live  # flags.9?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> StoryItemSkipped:
        
        flags = Int.read(b)
        
        close_friends = True if flags & (1 << 8) else False
        live = True if flags & (1 << 9) else False
        id = Int.read(b)
        
        date = Int.read(b)
        
        expire_date = Int.read(b)
        
        return StoryItemSkipped(id=id, date=date, expire_date=expire_date, close_friends=close_friends, live=live)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 8) if self.close_friends else 0
        flags |= (1 << 9) if self.live else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(Int(self.date))
        
        b.write(Int(self.expire_date))
        
        return b.getvalue()
