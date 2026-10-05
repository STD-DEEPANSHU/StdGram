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


class Search(TLObject["raw.base.contacts.Found"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``5F58D0F``

    Parameters:
        q (``str``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        broadcasts (``bool``, *optional*):
            N/A

        bots (``bool``, *optional*):
            N/A

    Returns:
        :obj:`contacts.Found <stdgram.raw.base.contacts.Found>`
    """

    __slots__: list[str] = ["q", "limit", "broadcasts", "bots"]

    ID = 0x5f58d0f
    QUALNAME = "functions.contacts.Search"

    def __init__(self, *, q: str, limit: int, broadcasts: bool | None = None, bots: bool | None = None) -> None:
        self.q = q  # string
        self.limit = limit  # int
        self.broadcasts = broadcasts  # flags.0?true
        self.bots = bots  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> Search:
        
        flags = Int.read(b)
        
        broadcasts = True if flags & (1 << 0) else False
        bots = True if flags & (1 << 1) else False
        q = String.read(b)
        
        limit = Int.read(b)
        
        return Search(q=q, limit=limit, broadcasts=broadcasts, bots=bots)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.broadcasts else 0
        flags |= (1 << 1) if self.bots else 0
        b.write(Int(flags))
        
        b.write(String(self.q))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
