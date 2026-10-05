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


class CheckUrlAuthMatchCode(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``C9A47B0B``

    Parameters:
        url (``str``):
            N/A

        match_code (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["url", "match_code"]

    ID = 0xc9a47b0b
    QUALNAME = "functions.messages.CheckUrlAuthMatchCode"

    def __init__(self, *, url: str, match_code: str) -> None:
        self.url = url  # string
        self.match_code = match_code  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> CheckUrlAuthMatchCode:
        # No flags
        
        url = String.read(b)
        
        match_code = String.read(b)
        
        return CheckUrlAuthMatchCode(url=url, match_code=match_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        b.write(String(self.match_code))
        
        return b.getvalue()
