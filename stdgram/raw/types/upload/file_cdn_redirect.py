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


class FileCdnRedirect(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.upload.File`.

    Details:
        - Layer: ``229``
        - ID: ``F18CDA44``

    Parameters:
        dc_id (``int`` ``32-bit``):
            N/A

        file_token (``bytes``):
            N/A

        encryption_key (``bytes``):
            N/A

        encryption_iv (``bytes``):
            N/A

        file_hashes (List of :obj:`FileHash <stdgram.raw.base.FileHash>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            upload.GetFile
    """

    __slots__: list[str] = ["dc_id", "file_token", "encryption_key", "encryption_iv", "file_hashes"]

    ID = 0xf18cda44
    QUALNAME = "types.upload.FileCdnRedirect"

    def __init__(self, *, dc_id: int, file_token: bytes, encryption_key: bytes, encryption_iv: bytes, file_hashes: list[raw.base.FileHash]) -> None:
        self.dc_id = dc_id  # int
        self.file_token = file_token  # bytes
        self.encryption_key = encryption_key  # bytes
        self.encryption_iv = encryption_iv  # bytes
        self.file_hashes = file_hashes  # Vector<FileHash>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> FileCdnRedirect:
        # No flags
        
        dc_id = Int.read(b)
        
        file_token = Bytes.read(b)
        
        encryption_key = Bytes.read(b)
        
        encryption_iv = Bytes.read(b)
        
        file_hashes = TLObject.read(b)
        
        return FileCdnRedirect(dc_id=dc_id, file_token=file_token, encryption_key=encryption_key, encryption_iv=encryption_iv, file_hashes=file_hashes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.dc_id))
        
        b.write(Bytes(self.file_token))
        
        b.write(Bytes(self.encryption_key))
        
        b.write(Bytes(self.encryption_iv))
        
        b.write(Vector(self.file_hashes))
        
        return b.getvalue()
