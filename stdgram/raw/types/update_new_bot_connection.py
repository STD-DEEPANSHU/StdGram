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


class UpdateNewBotConnection(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.Update`.

    Details:
        - Layer: ``229``
        - ID: ``B22083A6``

    Parameters:
        bot_id (``int`` ``64-bit``):
            N/A

        confirmed (``bool``, *optional*):
            N/A

        date (``int`` ``32-bit``, *optional*):
            N/A

        device (``str``, *optional*):
            N/A

        location (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["bot_id", "confirmed", "date", "device", "location"]

    ID = 0xb22083a6
    QUALNAME = "types.UpdateNewBotConnection"

    def __init__(self, *, bot_id: int, confirmed: bool | None = None, date: int | None = None, device: str | None = None, location: str | None = None) -> None:
        self.bot_id = bot_id  # long
        self.confirmed = confirmed  # flags.0?true
        self.date = date  # flags.1?int
        self.device = device  # flags.1?string
        self.location = location  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateNewBotConnection:
        
        flags = Int.read(b)
        
        confirmed = True if flags & (1 << 0) else False
        bot_id = Long.read(b)
        
        date = Int.read(b) if flags & (1 << 1) else None
        device = String.read(b) if flags & (1 << 1) else None
        location = String.read(b) if flags & (1 << 1) else None
        return UpdateNewBotConnection(bot_id=bot_id, confirmed=confirmed, date=date, device=device, location=location)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.confirmed else 0
        flags |= (1 << 1) if self.date is not None else 0
        flags |= (1 << 1) if self.device is not None else 0
        flags |= (1 << 1) if self.location is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.bot_id))
        
        if self.date is not None:
            b.write(Int(self.date))
        
        if self.device is not None:
            b.write(String(self.device))
        
        if self.location is not None:
            b.write(String(self.location))
        
        return b.getvalue()
