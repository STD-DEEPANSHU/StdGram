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


class UpdateBusinessLocation(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``9E6B131A``

    Parameters:
        geo_point (:obj:`InputGeoPoint <stdgram.raw.base.InputGeoPoint>`, *optional*):
            N/A

        address (``str``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["geo_point", "address"]

    ID = 0x9e6b131a
    QUALNAME = "functions.account.UpdateBusinessLocation"

    def __init__(self, *, geo_point: raw.base.InputGeoPoint | None = None, address: str | None = None) -> None:
        self.geo_point = geo_point  # flags.1?InputGeoPoint
        self.address = address  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateBusinessLocation:
        
        flags = Int.read(b)
        
        geo_point = TLObject.read(b) if flags & (1 << 1) else None
        
        address = String.read(b) if flags & (1 << 0) else None
        return UpdateBusinessLocation(geo_point=geo_point, address=address)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.geo_point is not None else 0
        flags |= (1 << 0) if self.address is not None else 0
        b.write(Int(flags))
        
        if self.geo_point is not None:
            b.write(self.geo_point.write())
        
        if self.address is not None:
            b.write(String(self.address))
        
        return b.getvalue()
