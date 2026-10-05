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


class AddChatUser(TLObject["raw.base.messages.InvitedUsers"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``CBC6D107``

    Parameters:
        chat_id (``int`` ``64-bit``):
            N/A

        user_id (:obj:`InputUser <stdgram.raw.base.InputUser>`):
            N/A

        fwd_limit (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`messages.InvitedUsers <stdgram.raw.base.messages.InvitedUsers>`
    """

    __slots__: list[str] = ["chat_id", "user_id", "fwd_limit"]

    ID = 0xcbc6d107
    QUALNAME = "functions.messages.AddChatUser"

    def __init__(self, *, chat_id: int, user_id: raw.base.InputUser, fwd_limit: int) -> None:
        self.chat_id = chat_id  # long
        self.user_id = user_id  # InputUser
        self.fwd_limit = fwd_limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> AddChatUser:
        # No flags
        
        chat_id = Long.read(b)
        
        user_id = TLObject.read(b)
        
        fwd_limit = Int.read(b)
        
        return AddChatUser(chat_id=chat_id, user_id=user_id, fwd_limit=fwd_limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.chat_id))
        
        b.write(self.user_id.write())
        
        b.write(Int(self.fwd_limit))
        
        return b.getvalue()
