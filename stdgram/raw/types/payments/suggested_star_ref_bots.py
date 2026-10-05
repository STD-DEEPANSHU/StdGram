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


class SuggestedStarRefBots(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.payments.SuggestedStarRefBots`.

    Details:
        - Layer: ``229``
        - ID: ``B4D5D859``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        suggested_bots (List of :obj:`StarRefProgram <stdgram.raw.base.StarRefProgram>`):
            N/A

        users (List of :obj:`User <stdgram.raw.base.User>`):
            N/A

        next_offset (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetSuggestedStarRefBots
    """

    __slots__: list[str] = ["count", "suggested_bots", "users", "next_offset"]

    ID = 0xb4d5d859
    QUALNAME = "types.payments.SuggestedStarRefBots"

    def __init__(self, *, count: int, suggested_bots: list[raw.base.StarRefProgram], users: list[raw.base.User], next_offset: str | None = None) -> None:
        self.count = count  # int
        self.suggested_bots = suggested_bots  # Vector<StarRefProgram>
        self.users = users  # Vector<User>
        self.next_offset = next_offset  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SuggestedStarRefBots:
        
        flags = Int.read(b)
        
        count = Int.read(b)
        
        suggested_bots = TLObject.read(b)
        
        users = TLObject.read(b)
        
        next_offset = String.read(b) if flags & (1 << 0) else None
        return SuggestedStarRefBots(count=count, suggested_bots=suggested_bots, users=users, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        b.write(Vector(self.suggested_bots))
        
        b.write(Vector(self.users))
        
        if self.next_offset is not None:
            b.write(String(self.next_offset))
        
        return b.getvalue()
