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


class RequestEncryption(TLObject["raw.base.EncryptedChat"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``F64DAF43``

    Parameters:
        user_id (:obj:`InputUser <stdgram.raw.base.InputUser>`):
            N/A

        random_id (``int`` ``32-bit``):
            N/A

        g_a (``bytes``):
            N/A

    Returns:
        :obj:`EncryptedChat <stdgram.raw.base.EncryptedChat>`
    """

    __slots__: list[str] = ["user_id", "random_id", "g_a"]

    ID = 0xf64daf43
    QUALNAME = "functions.messages.RequestEncryption"

    def __init__(self, *, user_id: raw.base.InputUser, random_id: int, g_a: bytes) -> None:
        self.user_id = user_id  # InputUser
        self.random_id = random_id  # int
        self.g_a = g_a  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> RequestEncryption:
        # No flags
        
        user_id = TLObject.read(b)
        
        random_id = Int.read(b)
        
        g_a = Bytes.read(b)
        
        return RequestEncryption(user_id=user_id, random_id=random_id, g_a=g_a)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.user_id.write())
        
        b.write(Int(self.random_id))
        
        b.write(Bytes(self.g_a))
        
        return b.getvalue()
