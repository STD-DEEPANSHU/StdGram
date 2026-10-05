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


class InputEncryptedFileBigUploaded(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputEncryptedFile`.

    Details:
        - Layer: ``229``
        - ID: ``2DC173C8``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        parts (``int`` ``32-bit``):
            N/A

        key_fingerprint (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["id", "parts", "key_fingerprint"]

    ID = 0x2dc173c8
    QUALNAME = "types.InputEncryptedFileBigUploaded"

    def __init__(self, *, id: int, parts: int, key_fingerprint: int) -> None:
        self.id = id  # long
        self.parts = parts  # int
        self.key_fingerprint = key_fingerprint  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputEncryptedFileBigUploaded:
        # No flags
        
        id = Long.read(b)
        
        parts = Int.read(b)
        
        key_fingerprint = Int.read(b)
        
        return InputEncryptedFileBigUploaded(id=id, parts=parts, key_fingerprint=key_fingerprint)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        b.write(Int(self.parts))
        
        b.write(Int(self.key_fingerprint))
        
        return b.getvalue()
