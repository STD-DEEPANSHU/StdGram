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


class Timezone(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.Timezone`.

    Details:
        - Layer: ``229``
        - ID: ``FF9289F5``

    Parameters:
        id (``str``):
            N/A

        name (``str``):
            N/A

        utc_offset (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["id", "name", "utc_offset"]

    ID = 0xff9289f5
    QUALNAME = "types.Timezone"

    def __init__(self, *, id: str, name: str, utc_offset: int) -> None:
        self.id = id  # string
        self.name = name  # string
        self.utc_offset = utc_offset  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> Timezone:
        # No flags
        
        id = String.read(b)
        
        name = String.read(b)
        
        utc_offset = Int.read(b)
        
        return Timezone(id=id, name=name, utc_offset=utc_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.id))
        
        b.write(String(self.name))
        
        b.write(Int(self.utc_offset))
        
        return b.getvalue()
