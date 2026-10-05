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


class MessageMediaGeoLive(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.MessageMedia`.

    Details:
        - Layer: ``229``
        - ID: ``B940C666``

    Parameters:
        geo (:obj:`GeoPoint <stdgram.raw.base.GeoPoint>`):
            N/A

        period (``int`` ``32-bit``):
            N/A

        heading (``int`` ``32-bit``, *optional*):
            N/A

        proximity_notification_radius (``int`` ``32-bit``, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: list[str] = ["geo", "period", "heading", "proximity_notification_radius"]

    ID = 0xb940c666
    QUALNAME = "types.MessageMediaGeoLive"

    def __init__(self, *, geo: raw.base.GeoPoint, period: int, heading: int | None = None, proximity_notification_radius: int | None = None) -> None:
        self.geo = geo  # GeoPoint
        self.period = period  # int
        self.heading = heading  # flags.0?int
        self.proximity_notification_radius = proximity_notification_radius  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> MessageMediaGeoLive:
        
        flags = Int.read(b)
        
        geo = TLObject.read(b)
        
        heading = Int.read(b) if flags & (1 << 0) else None
        period = Int.read(b)
        
        proximity_notification_radius = Int.read(b) if flags & (1 << 1) else None
        return MessageMediaGeoLive(geo=geo, period=period, heading=heading, proximity_notification_radius=proximity_notification_radius)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.heading is not None else 0
        flags |= (1 << 1) if self.proximity_notification_radius is not None else 0
        b.write(Int(flags))
        
        b.write(self.geo.write())
        
        if self.heading is not None:
            b.write(Int(self.heading))
        
        b.write(Int(self.period))
        
        if self.proximity_notification_radius is not None:
            b.write(Int(self.proximity_notification_radius))
        
        return b.getvalue()
