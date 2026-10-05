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


class CountryCode(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.help.CountryCode`.

    Details:
        - Layer: ``229``
        - ID: ``4203C5EF``

    Parameters:
        country_code (``str``):
            N/A

        prefixes (List of ``str``, *optional*):
            N/A

        patterns (List of ``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["country_code", "prefixes", "patterns"]

    ID = 0x4203c5ef
    QUALNAME = "types.help.CountryCode"

    def __init__(self, *, country_code: str, prefixes: list[str] | None = None, patterns: list[str] | None = None) -> None:
        self.country_code = country_code  # string
        self.prefixes = prefixes  # flags.0?Vector<string>
        self.patterns = patterns  # flags.1?Vector<string>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> CountryCode:
        
        flags = Int.read(b)
        
        country_code = String.read(b)
        
        prefixes = TLObject.read(b, String) if flags & (1 << 0) else []
        
        patterns = TLObject.read(b, String) if flags & (1 << 1) else []
        
        return CountryCode(country_code=country_code, prefixes=prefixes, patterns=patterns)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.prefixes else 0
        flags |= (1 << 1) if self.patterns else 0
        b.write(Int(flags))
        
        b.write(String(self.country_code))
        
        if self.prefixes is not None:
            b.write(Vector(self.prefixes, String))
        
        if self.patterns is not None:
            b.write(Vector(self.patterns, String))
        
        return b.getvalue()
