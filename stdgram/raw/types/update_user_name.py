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


class UpdateUserName(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.Update`.

    Details:
        - Layer: ``229``
        - ID: ``A7848924``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        first_name (``str``):
            N/A

        last_name (``str``):
            N/A

        usernames (List of :obj:`Username <stdgram.raw.base.Username>`):
            N/A

    """

    __slots__: list[str] = ["user_id", "first_name", "last_name", "usernames"]

    ID = 0xa7848924
    QUALNAME = "types.UpdateUserName"

    def __init__(self, *, user_id: int, first_name: str, last_name: str, usernames: list[raw.base.Username]) -> None:
        self.user_id = user_id  # long
        self.first_name = first_name  # string
        self.last_name = last_name  # string
        self.usernames = usernames  # Vector<Username>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateUserName:
        # No flags
        
        user_id = Long.read(b)
        
        first_name = String.read(b)
        
        last_name = String.read(b)
        
        usernames = TLObject.read(b)
        
        return UpdateUserName(user_id=user_id, first_name=first_name, last_name=last_name, usernames=usernames)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.user_id))
        
        b.write(String(self.first_name))
        
        b.write(String(self.last_name))
        
        b.write(Vector(self.usernames))
        
        return b.getvalue()
