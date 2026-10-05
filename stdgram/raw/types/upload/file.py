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


class File(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.upload.File`.

    Details:
        - Layer: ``229``
        - ID: ``96A18D5``

    Parameters:
        type (:obj:`storage.FileType <stdgram.raw.base.storage.FileType>`):
            N/A

        mtime (``int`` ``32-bit``):
            N/A

        bytes (``bytes``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            upload.GetFile
    """

    __slots__: list[str] = ["type", "mtime", "bytes"]

    ID = 0x96a18d5
    QUALNAME = "types.upload.File"

    def __init__(self, *, type: raw.base.storage.FileType, mtime: int, bytes: bytes) -> None:
        self.type = type  # storage.FileType
        self.mtime = mtime  # int
        self.bytes = bytes  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> File:
        # No flags
        
        type = TLObject.read(b)
        
        mtime = Int.read(b)
        
        bytes = Bytes.read(b)
        
        return File(type=type, mtime=mtime, bytes=bytes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.type.write())
        
        b.write(Int(self.mtime))
        
        b.write(Bytes(self.bytes))
        
        return b.getvalue()
