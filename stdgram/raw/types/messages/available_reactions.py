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


class AvailableReactions(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.messages.AvailableReactions`.

    Details:
        - Layer: ``229``
        - ID: ``768E3AAD``

    Parameters:
        hash (``int`` ``32-bit``):
            N/A

        reactions (List of :obj:`AvailableReaction <stdgram.raw.base.AvailableReaction>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAvailableReactions
    """

    __slots__: list[str] = ["hash", "reactions"]

    ID = 0x768e3aad
    QUALNAME = "types.messages.AvailableReactions"

    def __init__(self, *, hash: int, reactions: list[raw.base.AvailableReaction]) -> None:
        self.hash = hash  # int
        self.reactions = reactions  # Vector<AvailableReaction>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> AvailableReactions:
        # No flags
        
        hash = Int.read(b)
        
        reactions = TLObject.read(b)
        
        return AvailableReactions(hash=hash, reactions=reactions)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.hash))
        
        b.write(Vector(self.reactions))
        
        return b.getvalue()
