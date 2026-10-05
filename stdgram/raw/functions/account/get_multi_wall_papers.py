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


class GetMultiWallPapers(TLObject["list[raw.base.WallPaper]"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``65AD71DC``

    Parameters:
        wallpapers (List of :obj:`InputWallPaper <stdgram.raw.base.InputWallPaper>`):
            N/A

    Returns:
        List of :obj:`WallPaper <stdgram.raw.base.WallPaper>`
    """

    __slots__: list[str] = ["wallpapers"]

    ID = 0x65ad71dc
    QUALNAME = "functions.account.GetMultiWallPapers"

    def __init__(self, *, wallpapers: list[raw.base.InputWallPaper]) -> None:
        self.wallpapers = wallpapers  # Vector<InputWallPaper>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GetMultiWallPapers:
        # No flags
        
        wallpapers = TLObject.read(b)
        
        return GetMultiWallPapers(wallpapers=wallpapers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.wallpapers))
        
        return b.getvalue()
