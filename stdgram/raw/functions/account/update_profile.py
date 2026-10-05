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


class UpdateProfile(TLObject["raw.base.User"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``78515775``

    Parameters:
        first_name (``str``, *optional*):
            N/A

        last_name (``str``, *optional*):
            N/A

        about (``str``, *optional*):
            N/A

    Returns:
        :obj:`User <stdgram.raw.base.User>`
    """

    __slots__: list[str] = ["first_name", "last_name", "about"]

    ID = 0x78515775
    QUALNAME = "functions.account.UpdateProfile"

    def __init__(self, *, first_name: str | None = None, last_name: str | None = None, about: str | None = None) -> None:
        self.first_name = first_name  # flags.0?string
        self.last_name = last_name  # flags.1?string
        self.about = about  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateProfile:
        
        flags = Int.read(b)
        
        first_name = String.read(b) if flags & (1 << 0) else None
        last_name = String.read(b) if flags & (1 << 1) else None
        about = String.read(b) if flags & (1 << 2) else None
        return UpdateProfile(first_name=first_name, last_name=last_name, about=about)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.first_name is not None else 0
        flags |= (1 << 1) if self.last_name is not None else 0
        flags |= (1 << 2) if self.about is not None else 0
        b.write(Int(flags))
        
        if self.first_name is not None:
            b.write(String(self.first_name))
        
        if self.last_name is not None:
            b.write(String(self.last_name))
        
        if self.about is not None:
            b.write(String(self.about))
        
        return b.getvalue()
