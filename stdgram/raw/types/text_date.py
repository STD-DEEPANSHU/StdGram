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


class TextDate(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.RichText`.

    Details:
        - Layer: ``229``
        - ID: ``A5B45E2B``

    Parameters:
        text (:obj:`RichText <stdgram.raw.base.RichText>`):
            N/A

        date (``int`` ``32-bit``):
            N/A

        relative (``bool``, *optional*):
            N/A

        short_time (``bool``, *optional*):
            N/A

        long_time (``bool``, *optional*):
            N/A

        short_date (``bool``, *optional*):
            N/A

        long_date (``bool``, *optional*):
            N/A

        day_of_week (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["text", "date", "relative", "short_time", "long_time", "short_date", "long_date", "day_of_week"]

    ID = 0xa5b45e2b
    QUALNAME = "types.TextDate"

    def __init__(self, *, text: raw.base.RichText, date: int, relative: bool | None = None, short_time: bool | None = None, long_time: bool | None = None, short_date: bool | None = None, long_date: bool | None = None, day_of_week: bool | None = None) -> None:
        self.text = text  # RichText
        self.date = date  # int
        self.relative = relative  # flags.0?true
        self.short_time = short_time  # flags.1?true
        self.long_time = long_time  # flags.2?true
        self.short_date = short_date  # flags.3?true
        self.long_date = long_date  # flags.4?true
        self.day_of_week = day_of_week  # flags.5?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> TextDate:
        
        flags = Int.read(b)
        
        relative = True if flags & (1 << 0) else False
        short_time = True if flags & (1 << 1) else False
        long_time = True if flags & (1 << 2) else False
        short_date = True if flags & (1 << 3) else False
        long_date = True if flags & (1 << 4) else False
        day_of_week = True if flags & (1 << 5) else False
        text = TLObject.read(b)
        
        date = Int.read(b)
        
        return TextDate(text=text, date=date, relative=relative, short_time=short_time, long_time=long_time, short_date=short_date, long_date=long_date, day_of_week=day_of_week)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.relative else 0
        flags |= (1 << 1) if self.short_time else 0
        flags |= (1 << 2) if self.long_time else 0
        flags |= (1 << 3) if self.short_date else 0
        flags |= (1 << 4) if self.long_date else 0
        flags |= (1 << 5) if self.day_of_week else 0
        b.write(Int(flags))
        
        b.write(self.text.write())
        
        b.write(Int(self.date))
        
        return b.getvalue()
