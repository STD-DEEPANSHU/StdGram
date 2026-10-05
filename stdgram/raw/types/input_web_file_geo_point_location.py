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


class InputWebFileGeoPointLocation(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputWebFileLocation`.

    Details:
        - Layer: ``229``
        - ID: ``9F2221C9``

    Parameters:
        geo_point (:obj:`InputGeoPoint <stdgram.raw.base.InputGeoPoint>`):
            N/A

        access_hash (``int`` ``64-bit``):
            N/A

        w (``int`` ``32-bit``):
            N/A

        h (``int`` ``32-bit``):
            N/A

        zoom (``int`` ``32-bit``):
            N/A

        scale (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["geo_point", "access_hash", "w", "h", "zoom", "scale"]

    ID = 0x9f2221c9
    QUALNAME = "types.InputWebFileGeoPointLocation"

    def __init__(self, *, geo_point: raw.base.InputGeoPoint, access_hash: int, w: int, h: int, zoom: int, scale: int) -> None:
        self.geo_point = geo_point  # InputGeoPoint
        self.access_hash = access_hash  # long
        self.w = w  # int
        self.h = h  # int
        self.zoom = zoom  # int
        self.scale = scale  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputWebFileGeoPointLocation:
        # No flags
        
        geo_point = TLObject.read(b)
        
        access_hash = Long.read(b)
        
        w = Int.read(b)
        
        h = Int.read(b)
        
        zoom = Int.read(b)
        
        scale = Int.read(b)
        
        return InputWebFileGeoPointLocation(geo_point=geo_point, access_hash=access_hash, w=w, h=h, zoom=zoom, scale=scale)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.geo_point.write())
        
        b.write(Long(self.access_hash))
        
        b.write(Int(self.w))
        
        b.write(Int(self.h))
        
        b.write(Int(self.zoom))
        
        b.write(Int(self.scale))
        
        return b.getvalue()
