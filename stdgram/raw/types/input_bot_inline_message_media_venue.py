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


class InputBotInlineMessageMediaVenue(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputBotInlineMessage`.

    Details:
        - Layer: ``229``
        - ID: ``417BBF11``

    Parameters:
        geo_point (:obj:`InputGeoPoint <stdgram.raw.base.InputGeoPoint>`):
            N/A

        title (``str``):
            N/A

        address (``str``):
            N/A

        provider (``str``):
            N/A

        venue_id (``str``):
            N/A

        venue_type (``str``):
            N/A

        reply_markup (:obj:`ReplyMarkup <stdgram.raw.base.ReplyMarkup>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["geo_point", "title", "address", "provider", "venue_id", "venue_type", "reply_markup"]

    ID = 0x417bbf11
    QUALNAME = "types.InputBotInlineMessageMediaVenue"

    def __init__(self, *, geo_point: raw.base.InputGeoPoint, title: str, address: str, provider: str, venue_id: str, venue_type: str, reply_markup: raw.base.ReplyMarkup | None = None) -> None:
        self.geo_point = geo_point  # InputGeoPoint
        self.title = title  # string
        self.address = address  # string
        self.provider = provider  # string
        self.venue_id = venue_id  # string
        self.venue_type = venue_type  # string
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputBotInlineMessageMediaVenue:
        
        flags = Int.read(b)
        
        geo_point = TLObject.read(b)
        
        title = String.read(b)
        
        address = String.read(b)
        
        provider = String.read(b)
        
        venue_id = String.read(b)
        
        venue_type = String.read(b)
        
        reply_markup = TLObject.read(b) if flags & (1 << 2) else None
        
        return InputBotInlineMessageMediaVenue(geo_point=geo_point, title=title, address=address, provider=provider, venue_id=venue_id, venue_type=venue_type, reply_markup=reply_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        b.write(Int(flags))
        
        b.write(self.geo_point.write())
        
        b.write(String(self.title))
        
        b.write(String(self.address))
        
        b.write(String(self.provider))
        
        b.write(String(self.venue_id))
        
        b.write(String(self.venue_type))
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        return b.getvalue()
