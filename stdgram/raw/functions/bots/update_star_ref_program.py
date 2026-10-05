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


class UpdateStarRefProgram(TLObject["raw.base.StarRefProgram"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``778B5AB3``

    Parameters:
        bot (:obj:`InputUser <stdgram.raw.base.InputUser>`):
            N/A

        commission_permille (``int`` ``32-bit``):
            N/A

        duration_months (``int`` ``32-bit``, *optional*):
            N/A

    Returns:
        :obj:`StarRefProgram <stdgram.raw.base.StarRefProgram>`
    """

    __slots__: list[str] = ["bot", "commission_permille", "duration_months"]

    ID = 0x778b5ab3
    QUALNAME = "functions.bots.UpdateStarRefProgram"

    def __init__(self, *, bot: raw.base.InputUser, commission_permille: int, duration_months: int | None = None) -> None:
        self.bot = bot  # InputUser
        self.commission_permille = commission_permille  # int
        self.duration_months = duration_months  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateStarRefProgram:
        
        flags = Int.read(b)
        
        bot = TLObject.read(b)
        
        commission_permille = Int.read(b)
        
        duration_months = Int.read(b) if flags & (1 << 0) else None
        return UpdateStarRefProgram(bot=bot, commission_permille=commission_permille, duration_months=duration_months)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.duration_months is not None else 0
        b.write(Int(flags))
        
        b.write(self.bot.write())
        
        b.write(Int(self.commission_permille))
        
        if self.duration_months is not None:
            b.write(Int(self.duration_months))
        
        return b.getvalue()
