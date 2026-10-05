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


class SendEncrypted(TLObject["raw.base.messages.SentEncryptedMessage"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``44FA7A15``

    Parameters:
        peer (:obj:`InputEncryptedChat <stdgram.raw.base.InputEncryptedChat>`):
            N/A

        random_id (``int`` ``64-bit``):
            N/A

        data (``bytes``):
            N/A

        silent (``bool``, *optional*):
            N/A

    Returns:
        :obj:`messages.SentEncryptedMessage <stdgram.raw.base.messages.SentEncryptedMessage>`
    """

    __slots__: list[str] = ["peer", "random_id", "data", "silent"]

    ID = 0x44fa7a15
    QUALNAME = "functions.messages.SendEncrypted"

    def __init__(self, *, peer: raw.base.InputEncryptedChat, random_id: int, data: bytes, silent: bool | None = None) -> None:
        self.peer = peer  # InputEncryptedChat
        self.random_id = random_id  # long
        self.data = data  # bytes
        self.silent = silent  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SendEncrypted:
        
        flags = Int.read(b)
        
        silent = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        random_id = Long.read(b)
        
        data = Bytes.read(b)
        
        return SendEncrypted(peer=peer, random_id=random_id, data=data, silent=silent)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.silent else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Long(self.random_id))
        
        b.write(Bytes(self.data))
        
        return b.getvalue()
