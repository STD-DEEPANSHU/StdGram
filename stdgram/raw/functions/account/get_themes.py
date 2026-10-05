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


class GetThemes(TLObject["raw.base.account.Themes"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``7206E458``

    Parameters:
        format (``str``):
            N/A

        hash (``int`` ``64-bit``):
            N/A

    Returns:
        :obj:`account.Themes <stdgram.raw.base.account.Themes>`
    """

    __slots__: list[str] = ["format", "hash"]

    ID = 0x7206e458
    QUALNAME = "functions.account.GetThemes"

    def __init__(self, *, format: str, hash: int) -> None:
        self.format = format  # string
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GetThemes:
        # No flags
        
        format = String.read(b)
        
        hash = Long.read(b)
        
        return GetThemes(format=format, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.format))
        
        b.write(Long(self.hash))
        
        return b.getvalue()
