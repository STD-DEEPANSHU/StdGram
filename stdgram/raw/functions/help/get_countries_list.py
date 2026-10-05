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


class GetCountriesList(TLObject["raw.base.help.CountriesList"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``735787A8``

    Parameters:
        lang_code (``str``):
            N/A

        hash (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`help.CountriesList <stdgram.raw.base.help.CountriesList>`
    """

    __slots__: list[str] = ["lang_code", "hash"]

    ID = 0x735787a8
    QUALNAME = "functions.help.GetCountriesList"

    def __init__(self, *, lang_code: str, hash: int) -> None:
        self.lang_code = lang_code  # string
        self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GetCountriesList:
        # No flags
        
        lang_code = String.read(b)
        
        hash = Int.read(b)
        
        return GetCountriesList(lang_code=lang_code, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.lang_code))
        
        b.write(Int(self.hash))
        
        return b.getvalue()
