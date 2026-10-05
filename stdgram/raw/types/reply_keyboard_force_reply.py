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


class ReplyKeyboardForceReply(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.ReplyMarkup`.

    Details:
        - Layer: ``229``
        - ID: ``86B40B08``

    Parameters:
        single_use (``bool``, *optional*):
            N/A

        selective (``bool``, *optional*):
            N/A

        placeholder (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["single_use", "selective", "placeholder"]

    ID = 0x86b40b08
    QUALNAME = "types.ReplyKeyboardForceReply"

    def __init__(self, *, single_use: bool | None = None, selective: bool | None = None, placeholder: str | None = None) -> None:
        self.single_use = single_use  # flags.1?true
        self.selective = selective  # flags.2?true
        self.placeholder = placeholder  # flags.3?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> ReplyKeyboardForceReply:
        
        flags = Int.read(b)
        
        single_use = True if flags & (1 << 1) else False
        selective = True if flags & (1 << 2) else False
        placeholder = String.read(b) if flags & (1 << 3) else None
        return ReplyKeyboardForceReply(single_use=single_use, selective=selective, placeholder=placeholder)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.single_use else 0
        flags |= (1 << 2) if self.selective else 0
        flags |= (1 << 3) if self.placeholder is not None else 0
        b.write(Int(flags))
        
        if self.placeholder is not None:
            b.write(String(self.placeholder))
        
        return b.getvalue()
