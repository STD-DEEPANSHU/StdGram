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


class SearchPostsFlood(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.SearchPostsFlood`.

    Details:
        - Layer: ``229``
        - ID: ``3E0B5B6A``

    Parameters:
        total_daily (``int`` ``32-bit``):
            N/A

        remains (``int`` ``32-bit``):
            N/A

        stars_amount (``int`` ``64-bit``):
            N/A

        query_is_free (``bool``, *optional*):
            N/A

        wait_till (``int`` ``32-bit``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            channels.CheckSearchPostsFlood
    """

    __slots__: list[str] = ["total_daily", "remains", "stars_amount", "query_is_free", "wait_till"]

    ID = 0x3e0b5b6a
    QUALNAME = "types.SearchPostsFlood"

    def __init__(self, *, total_daily: int, remains: int, stars_amount: int, query_is_free: bool | None = None, wait_till: int | None = None) -> None:
        self.total_daily = total_daily  # int
        self.remains = remains  # int
        self.stars_amount = stars_amount  # long
        self.query_is_free = query_is_free  # flags.0?true
        self.wait_till = wait_till  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SearchPostsFlood:
        
        flags = Int.read(b)
        
        query_is_free = True if flags & (1 << 0) else False
        total_daily = Int.read(b)
        
        remains = Int.read(b)
        
        wait_till = Int.read(b) if flags & (1 << 1) else None
        stars_amount = Long.read(b)
        
        return SearchPostsFlood(total_daily=total_daily, remains=remains, stars_amount=stars_amount, query_is_free=query_is_free, wait_till=wait_till)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.query_is_free else 0
        flags |= (1 << 1) if self.wait_till is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.total_daily))
        
        b.write(Int(self.remains))
        
        if self.wait_till is not None:
            b.write(Int(self.wait_till))
        
        b.write(Long(self.stars_amount))
        
        return b.getvalue()
