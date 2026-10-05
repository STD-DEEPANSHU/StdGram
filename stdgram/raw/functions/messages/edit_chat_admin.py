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


class EditChatAdmin(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``A85BD1C2``

    Parameters:
        chat_id (``int`` ``64-bit``):
            N/A

        user_id (:obj:`InputUser <stdgram.raw.base.InputUser>`):
            N/A

        is_admin (``bool``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["chat_id", "user_id", "is_admin"]

    ID = 0xa85bd1c2
    QUALNAME = "functions.messages.EditChatAdmin"

    def __init__(self, *, chat_id: int, user_id: raw.base.InputUser, is_admin: bool) -> None:
        self.chat_id = chat_id  # long
        self.user_id = user_id  # InputUser
        self.is_admin = is_admin  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> EditChatAdmin:
        # No flags
        
        chat_id = Long.read(b)
        
        user_id = TLObject.read(b)
        
        is_admin = Bool.read(b)
        
        return EditChatAdmin(chat_id=chat_id, user_id=user_id, is_admin=is_admin)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.chat_id))
        
        b.write(self.user_id.write())
        
        b.write(Bool(self.is_admin))
        
        return b.getvalue()
