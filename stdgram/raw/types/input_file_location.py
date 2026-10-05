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


class InputFileLocation(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputFileLocation`.

    Details:
        - Layer: ``229``
        - ID: ``DFDAABE1``

    Parameters:
        volume_id (``int`` ``64-bit``):
            N/A

        local_id (``int`` ``32-bit``):
            N/A

        secret (``int`` ``64-bit``):
            N/A

        file_reference (``bytes``):
            N/A

    """

    __slots__: list[str] = ["volume_id", "local_id", "secret", "file_reference"]

    ID = 0xdfdaabe1
    QUALNAME = "types.InputFileLocation"

    def __init__(self, *, volume_id: int, local_id: int, secret: int, file_reference: bytes) -> None:
        self.volume_id = volume_id  # long
        self.local_id = local_id  # int
        self.secret = secret  # long
        self.file_reference = file_reference  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputFileLocation:
        # No flags
        
        volume_id = Long.read(b)
        
        local_id = Int.read(b)
        
        secret = Long.read(b)
        
        file_reference = Bytes.read(b)
        
        return InputFileLocation(volume_id=volume_id, local_id=local_id, secret=secret, file_reference=file_reference)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.volume_id))
        
        b.write(Int(self.local_id))
        
        b.write(Long(self.secret))
        
        b.write(Bytes(self.file_reference))
        
        return b.getvalue()
