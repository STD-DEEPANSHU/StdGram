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


class MessageMediaGiveaway(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.MessageMedia`.

    Details:
        - Layer: ``229``
        - ID: ``AA073BEB``

    Parameters:
        channels (List of ``int`` ``64-bit``):
            N/A

        quantity (``int`` ``32-bit``):
            N/A

        until_date (``int`` ``32-bit``):
            N/A

        only_new_subscribers (``bool``, *optional*):
            N/A

        winners_are_visible (``bool``, *optional*):
            N/A

        countries_iso2 (List of ``str``, *optional*):
            N/A

        prize_description (``str``, *optional*):
            N/A

        months (``int`` ``32-bit``, *optional*):
            N/A

        stars (``int`` ``64-bit``, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: list[str] = ["channels", "quantity", "until_date", "only_new_subscribers", "winners_are_visible", "countries_iso2", "prize_description", "months", "stars"]

    ID = 0xaa073beb
    QUALNAME = "types.MessageMediaGiveaway"

    def __init__(self, *, channels: list[int], quantity: int, until_date: int, only_new_subscribers: bool | None = None, winners_are_visible: bool | None = None, countries_iso2: list[str] | None = None, prize_description: str | None = None, months: int | None = None, stars: int | None = None) -> None:
        self.channels = channels  # Vector<long>
        self.quantity = quantity  # int
        self.until_date = until_date  # int
        self.only_new_subscribers = only_new_subscribers  # flags.0?true
        self.winners_are_visible = winners_are_visible  # flags.2?true
        self.countries_iso2 = countries_iso2  # flags.1?Vector<string>
        self.prize_description = prize_description  # flags.3?string
        self.months = months  # flags.4?int
        self.stars = stars  # flags.5?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> MessageMediaGiveaway:
        
        flags = Int.read(b)
        
        only_new_subscribers = True if flags & (1 << 0) else False
        winners_are_visible = True if flags & (1 << 2) else False
        channels = TLObject.read(b, Long)
        
        countries_iso2 = TLObject.read(b, String) if flags & (1 << 1) else []
        
        prize_description = String.read(b) if flags & (1 << 3) else None
        quantity = Int.read(b)
        
        months = Int.read(b) if flags & (1 << 4) else None
        stars = Long.read(b) if flags & (1 << 5) else None
        until_date = Int.read(b)
        
        return MessageMediaGiveaway(channels=channels, quantity=quantity, until_date=until_date, only_new_subscribers=only_new_subscribers, winners_are_visible=winners_are_visible, countries_iso2=countries_iso2, prize_description=prize_description, months=months, stars=stars)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.only_new_subscribers else 0
        flags |= (1 << 2) if self.winners_are_visible else 0
        flags |= (1 << 1) if self.countries_iso2 else 0
        flags |= (1 << 3) if self.prize_description is not None else 0
        flags |= (1 << 4) if self.months is not None else 0
        flags |= (1 << 5) if self.stars is not None else 0
        b.write(Int(flags))
        
        b.write(Vector(self.channels, Long))
        
        if self.countries_iso2 is not None:
            b.write(Vector(self.countries_iso2, String))
        
        if self.prize_description is not None:
            b.write(String(self.prize_description))
        
        b.write(Int(self.quantity))
        
        if self.months is not None:
            b.write(Int(self.months))
        
        if self.stars is not None:
            b.write(Long(self.stars))
        
        b.write(Int(self.until_date))
        
        return b.getvalue()
