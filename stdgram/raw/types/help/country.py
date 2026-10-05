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


class Country(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.help.Country`.

    Details:
        - Layer: ``229``
        - ID: ``C3878E23``

    Parameters:
        iso2 (``str``):
            N/A

        default_name (``str``):
            N/A

        country_codes (List of :obj:`help.CountryCode <stdgram.raw.base.help.CountryCode>`):
            N/A

        hidden (``bool``, *optional*):
            N/A

        name (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["iso2", "default_name", "country_codes", "hidden", "name"]

    ID = 0xc3878e23
    QUALNAME = "types.help.Country"

    def __init__(self, *, iso2: str, default_name: str, country_codes: list[raw.base.help.CountryCode], hidden: bool | None = None, name: str | None = None) -> None:
        self.iso2 = iso2  # string
        self.default_name = default_name  # string
        self.country_codes = country_codes  # Vector<help.CountryCode>
        self.hidden = hidden  # flags.0?true
        self.name = name  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> Country:
        
        flags = Int.read(b)
        
        hidden = True if flags & (1 << 0) else False
        iso2 = String.read(b)
        
        default_name = String.read(b)
        
        name = String.read(b) if flags & (1 << 1) else None
        country_codes = TLObject.read(b)
        
        return Country(iso2=iso2, default_name=default_name, country_codes=country_codes, hidden=hidden, name=name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.hidden else 0
        flags |= (1 << 1) if self.name is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.iso2))
        
        b.write(String(self.default_name))
        
        if self.name is not None:
            b.write(String(self.name))
        
        b.write(Vector(self.country_codes))
        
        return b.getvalue()
