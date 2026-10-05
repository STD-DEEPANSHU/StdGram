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


class NearestDc(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.NearestDc`.

    Details:
        - Layer: ``229``
        - ID: ``8E1A1775``

    Parameters:
        country (``str``):
            N/A

        this_dc (``int`` ``32-bit``):
            N/A

        nearest_dc (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetNearestDc
    """

    __slots__: list[str] = ["country", "this_dc", "nearest_dc"]

    ID = 0x8e1a1775
    QUALNAME = "types.NearestDc"

    def __init__(self, *, country: str, this_dc: int, nearest_dc: int) -> None:
        self.country = country  # string
        self.this_dc = this_dc  # int
        self.nearest_dc = nearest_dc  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> NearestDc:
        # No flags
        
        country = String.read(b)
        
        this_dc = Int.read(b)
        
        nearest_dc = Int.read(b)
        
        return NearestDc(country=country, this_dc=this_dc, nearest_dc=nearest_dc)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.country))
        
        b.write(Int(self.this_dc))
        
        b.write(Int(self.nearest_dc))
        
        return b.getvalue()
