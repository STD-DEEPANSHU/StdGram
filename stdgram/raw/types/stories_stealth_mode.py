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


class StoriesStealthMode(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.StoriesStealthMode`.

    Details:
        - Layer: ``229``
        - ID: ``712E27FD``

    Parameters:
        active_until_date (``int`` ``32-bit``, *optional*):
            N/A

        cooldown_until_date (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: list[str] = ["active_until_date", "cooldown_until_date"]

    ID = 0x712e27fd
    QUALNAME = "types.StoriesStealthMode"

    def __init__(self, *, active_until_date: int | None = None, cooldown_until_date: int | None = None) -> None:
        self.active_until_date = active_until_date  # flags.0?int
        self.cooldown_until_date = cooldown_until_date  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> StoriesStealthMode:
        
        flags = Int.read(b)
        
        active_until_date = Int.read(b) if flags & (1 << 0) else None
        cooldown_until_date = Int.read(b) if flags & (1 << 1) else None
        return StoriesStealthMode(active_until_date=active_until_date, cooldown_until_date=cooldown_until_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.active_until_date is not None else 0
        flags |= (1 << 1) if self.cooldown_until_date is not None else 0
        b.write(Int(flags))
        
        if self.active_until_date is not None:
            b.write(Int(self.active_until_date))
        
        if self.cooldown_until_date is not None:
            b.write(Int(self.cooldown_until_date))
        
        return b.getvalue()
