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


class GetCommonChats(TLObject["raw.base.messages.Chats"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``E40CA104``

    Parameters:
        user_id (:obj:`InputUser <stdgram.raw.base.InputUser>`):
            N/A

        max_id (``int`` ``64-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`messages.Chats <stdgram.raw.base.messages.Chats>`
    """

    __slots__: list[str] = ["user_id", "max_id", "limit"]

    ID = 0xe40ca104
    QUALNAME = "functions.messages.GetCommonChats"

    def __init__(self, *, user_id: raw.base.InputUser, max_id: int, limit: int) -> None:
        self.user_id = user_id  # InputUser
        self.max_id = max_id  # long
        self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GetCommonChats:
        # No flags
        
        user_id = TLObject.read(b)
        
        max_id = Long.read(b)
        
        limit = Int.read(b)
        
        return GetCommonChats(user_id=user_id, max_id=max_id, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.user_id.write())
        
        b.write(Long(self.max_id))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
