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


class GetCdnFile(TLObject["raw.base.upload.CdnFile"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``395F69DA``

    Parameters:
        file_token (``bytes``):
            N/A

        offset (``int`` ``64-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`upload.CdnFile <stdgram.raw.base.upload.CdnFile>`
    """

    __slots__: list[str] = ["file_token", "offset", "limit"]

    ID = 0x395f69da
    QUALNAME = "functions.upload.GetCdnFile"

    def __init__(self, *, file_token: bytes, offset: int, limit: int) -> None:
        self.file_token = file_token  # bytes
        self.offset = offset  # long
        self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GetCdnFile:
        # No flags
        
        file_token = Bytes.read(b)
        
        offset = Long.read(b)
        
        limit = Int.read(b)
        
        return GetCdnFile(file_token=file_token, offset=offset, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.file_token))
        
        b.write(Long(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
