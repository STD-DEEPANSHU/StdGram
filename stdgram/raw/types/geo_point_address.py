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


class GeoPointAddress(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.GeoPointAddress`.

    Details:
        - Layer: ``229``
        - ID: ``DE4C5D93``

    Parameters:
        country_iso2 (``str``):
            N/A

        state (``str``, *optional*):
            N/A

        city (``str``, *optional*):
            N/A

        street (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["country_iso2", "state", "city", "street"]

    ID = 0xde4c5d93
    QUALNAME = "types.GeoPointAddress"

    def __init__(self, *, country_iso2: str, state: str | None = None, city: str | None = None, street: str | None = None) -> None:
        self.country_iso2 = country_iso2  # string
        self.state = state  # flags.0?string
        self.city = city  # flags.1?string
        self.street = street  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GeoPointAddress:
        
        flags = Int.read(b)
        
        country_iso2 = String.read(b)
        
        state = String.read(b) if flags & (1 << 0) else None
        city = String.read(b) if flags & (1 << 1) else None
        street = String.read(b) if flags & (1 << 2) else None
        return GeoPointAddress(country_iso2=country_iso2, state=state, city=city, street=street)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.state is not None else 0
        flags |= (1 << 1) if self.city is not None else 0
        flags |= (1 << 2) if self.street is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.country_iso2))
        
        if self.state is not None:
            b.write(String(self.state))
        
        if self.city is not None:
            b.write(String(self.city))
        
        if self.street is not None:
            b.write(String(self.street))
        
        return b.getvalue()
