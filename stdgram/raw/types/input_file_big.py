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


class InputFileBig(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputFile`.

    Details:
        - Layer: ``229``
        - ID: ``FA4F0BB5``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        parts (``int`` ``32-bit``):
            N/A

        name (``str``):
            N/A

    """

    __slots__: list[str] = ["id", "parts", "name"]

    ID = 0xfa4f0bb5
    QUALNAME = "types.InputFileBig"

    def __init__(self, *, id: int, parts: int, name: str) -> None:
        self.id = id  # long
        self.parts = parts  # int
        self.name = name  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputFileBig:
        # No flags
        
        id = Long.read(b)
        
        parts = Int.read(b)
        
        name = String.read(b)
        
        return InputFileBig(id=id, parts=parts, name=name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        b.write(Int(self.parts))
        
        b.write(String(self.name))
        
        return b.getvalue()
