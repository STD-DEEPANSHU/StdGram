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


class UpdateColor(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``684D214E``

    Parameters:
        for_profile (``bool``, *optional*):
            N/A

        color (:obj:`PeerColor <stdgram.raw.base.PeerColor>`, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["for_profile", "color"]

    ID = 0x684d214e
    QUALNAME = "functions.account.UpdateColor"

    def __init__(self, *, for_profile: bool | None = None, color: raw.base.PeerColor | None = None) -> None:
        self.for_profile = for_profile  # flags.1?true
        self.color = color  # flags.2?PeerColor

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateColor:
        
        flags = Int.read(b)
        
        for_profile = True if flags & (1 << 1) else False
        color = TLObject.read(b) if flags & (1 << 2) else None
        
        return UpdateColor(for_profile=for_profile, color=color)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.for_profile else 0
        flags |= (1 << 2) if self.color is not None else 0
        b.write(Int(flags))
        
        if self.color is not None:
            b.write(self.color.write())
        
        return b.getvalue()
