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


class SearchCounter(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.messages.SearchCounter`.

    Details:
        - Layer: ``229``
        - ID: ``E844EBFF``

    Parameters:
        filter (:obj:`MessagesFilter <stdgram.raw.base.MessagesFilter>`):
            N/A

        count (``int`` ``32-bit``):
            N/A

        inexact (``bool``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSearchCounters
    """

    __slots__: list[str] = ["filter", "count", "inexact"]

    ID = 0xe844ebff
    QUALNAME = "types.messages.SearchCounter"

    def __init__(self, *, filter: raw.base.MessagesFilter, count: int, inexact: bool | None = None) -> None:
        self.filter = filter  # MessagesFilter
        self.count = count  # int
        self.inexact = inexact  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SearchCounter:
        
        flags = Int.read(b)
        
        inexact = True if flags & (1 << 1) else False
        filter = TLObject.read(b)
        
        count = Int.read(b)
        
        return SearchCounter(filter=filter, count=count, inexact=inexact)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.inexact else 0
        b.write(Int(flags))
        
        b.write(self.filter.write())
        
        b.write(Int(self.count))
        
        return b.getvalue()
