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


class PostAddress(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.PostAddress`.

    Details:
        - Layer: ``229``
        - ID: ``1E8CAAEB``

    Parameters:
        street_line1 (``str``):
            N/A

        street_line2 (``str``):
            N/A

        city (``str``):
            N/A

        state (``str``):
            N/A

        country_iso2 (``str``):
            N/A

        post_code (``str``):
            N/A

    """

    __slots__: list[str] = ["street_line1", "street_line2", "city", "state", "country_iso2", "post_code"]

    ID = 0x1e8caaeb
    QUALNAME = "types.PostAddress"

    def __init__(self, *, street_line1: str, street_line2: str, city: str, state: str, country_iso2: str, post_code: str) -> None:
        self.street_line1 = street_line1  # string
        self.street_line2 = street_line2  # string
        self.city = city  # string
        self.state = state  # string
        self.country_iso2 = country_iso2  # string
        self.post_code = post_code  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> PostAddress:
        # No flags
        
        street_line1 = String.read(b)
        
        street_line2 = String.read(b)
        
        city = String.read(b)
        
        state = String.read(b)
        
        country_iso2 = String.read(b)
        
        post_code = String.read(b)
        
        return PostAddress(street_line1=street_line1, street_line2=street_line2, city=city, state=state, country_iso2=country_iso2, post_code=post_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.street_line1))
        
        b.write(String(self.street_line2))
        
        b.write(String(self.city))
        
        b.write(String(self.state))
        
        b.write(String(self.country_iso2))
        
        b.write(String(self.post_code))
        
        return b.getvalue()
