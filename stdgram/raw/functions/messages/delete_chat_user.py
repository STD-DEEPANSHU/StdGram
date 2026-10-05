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


class DeleteChatUser(TLObject["raw.base.Updates"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``A2185CAB``

    Parameters:
        chat_id (``int`` ``64-bit``):
            N/A

        user_id (:obj:`InputUser <stdgram.raw.base.InputUser>`):
            N/A

        revoke_history (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <stdgram.raw.base.Updates>`
    """

    __slots__: list[str] = ["chat_id", "user_id", "revoke_history"]

    ID = 0xa2185cab
    QUALNAME = "functions.messages.DeleteChatUser"

    def __init__(self, *, chat_id: int, user_id: raw.base.InputUser, revoke_history: bool | None = None) -> None:
        self.chat_id = chat_id  # long
        self.user_id = user_id  # InputUser
        self.revoke_history = revoke_history  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> DeleteChatUser:
        
        flags = Int.read(b)
        
        revoke_history = True if flags & (1 << 0) else False
        chat_id = Long.read(b)
        
        user_id = TLObject.read(b)
        
        return DeleteChatUser(chat_id=chat_id, user_id=user_id, revoke_history=revoke_history)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.revoke_history else 0
        b.write(Int(flags))
        
        b.write(Long(self.chat_id))
        
        b.write(self.user_id.write())
        
        return b.getvalue()
