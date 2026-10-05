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


class PeerColors(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.help.PeerColors`.

    Details:
        - Layer: ``229``
        - ID: ``F8ED08``

    Parameters:
        hash (``int`` ``32-bit``):
            N/A

        colors (List of :obj:`help.PeerColorOption <stdgram.raw.base.help.PeerColorOption>`):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetPeerColors
            help.GetPeerProfileColors
    """

    __slots__: list[str] = ["hash", "colors"]

    ID = 0xf8ed08
    QUALNAME = "types.help.PeerColors"

    def __init__(self, *, hash: int, colors: list[raw.base.help.PeerColorOption]) -> None:
        self.hash = hash  # int
        self.colors = colors  # Vector<help.PeerColorOption>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> PeerColors:
        # No flags
        
        hash = Int.read(b)
        
        colors = TLObject.read(b)
        
        return PeerColors(hash=hash, colors=colors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.hash))
        
        b.write(Vector(self.colors))
        
        return b.getvalue()
