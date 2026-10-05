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


class UpdateGroupCallEncryptedMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.Update`.

    Details:
        - Layer: ``229``
        - ID: ``C957A766``

    Parameters:
        call (:obj:`InputGroupCall <stdgram.raw.base.InputGroupCall>`):
            N/A

        from_id (:obj:`Peer <stdgram.raw.base.Peer>`):
            N/A

        encrypted_message (``bytes``):
            N/A

    """

    __slots__: list[str] = ["call", "from_id", "encrypted_message"]

    ID = 0xc957a766
    QUALNAME = "types.UpdateGroupCallEncryptedMessage"

    def __init__(self, *, call: raw.base.InputGroupCall, from_id: raw.base.Peer, encrypted_message: bytes) -> None:
        self.call = call  # InputGroupCall
        self.from_id = from_id  # Peer
        self.encrypted_message = encrypted_message  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateGroupCallEncryptedMessage:
        # No flags
        
        call = TLObject.read(b)
        
        from_id = TLObject.read(b)
        
        encrypted_message = Bytes.read(b)
        
        return UpdateGroupCallEncryptedMessage(call=call, from_id=from_id, encrypted_message=encrypted_message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.call.write())
        
        b.write(self.from_id.write())
        
        b.write(Bytes(self.encrypted_message))
        
        return b.getvalue()
