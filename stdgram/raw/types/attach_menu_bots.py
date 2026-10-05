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


class AttachMenuBots(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.AttachMenuBots`.

    Details:
        - Layer: ``229``
        - ID: ``3C4301C0``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

        bots (List of :obj:`AttachMenuBot <stdgram.raw.base.AttachMenuBot>`):
            N/A

        users (List of :obj:`User <stdgram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAttachMenuBots
    """

    __slots__: list[str] = ["hash", "bots", "users"]

    ID = 0x3c4301c0
    QUALNAME = "types.AttachMenuBots"

    def __init__(self, *, hash: int, bots: list[raw.base.AttachMenuBot], users: list[raw.base.User]) -> None:
        self.hash = hash  # long
        self.bots = bots  # Vector<AttachMenuBot>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> AttachMenuBots:
        # No flags
        
        hash = Long.read(b)
        
        bots = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return AttachMenuBots(hash=hash, bots=bots, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Vector(self.bots))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
