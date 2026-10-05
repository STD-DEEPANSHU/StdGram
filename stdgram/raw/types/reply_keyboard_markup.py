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


class ReplyKeyboardMarkup(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.ReplyMarkup`.

    Details:
        - Layer: ``229``
        - ID: ``85DD99D1``

    Parameters:
        rows (List of :obj:`KeyboardButtonRow <stdgram.raw.base.KeyboardButtonRow>`):
            N/A

        resize (``bool``, *optional*):
            N/A

        single_use (``bool``, *optional*):
            N/A

        selective (``bool``, *optional*):
            N/A

        persistent (``bool``, *optional*):
            N/A

        force_reply (``bool``, *optional*):
            N/A

        placeholder (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["rows", "resize", "single_use", "selective", "persistent", "force_reply", "placeholder"]

    ID = 0x85dd99d1
    QUALNAME = "types.ReplyKeyboardMarkup"

    def __init__(self, *, rows: list[raw.base.KeyboardButtonRow], resize: bool | None = None, single_use: bool | None = None, selective: bool | None = None, persistent: bool | None = None, force_reply: bool | None = None, placeholder: str | None = None) -> None:
        self.rows = rows  # Vector<KeyboardButtonRow>
        self.resize = resize  # flags.0?true
        self.single_use = single_use  # flags.1?true
        self.selective = selective  # flags.2?true
        self.persistent = persistent  # flags.4?true
        self.force_reply = force_reply  # flags.5?true
        self.placeholder = placeholder  # flags.3?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> ReplyKeyboardMarkup:
        
        flags = Int.read(b)
        
        resize = True if flags & (1 << 0) else False
        single_use = True if flags & (1 << 1) else False
        selective = True if flags & (1 << 2) else False
        persistent = True if flags & (1 << 4) else False
        force_reply = True if flags & (1 << 5) else False
        rows = TLObject.read(b)
        
        placeholder = String.read(b) if flags & (1 << 3) else None
        return ReplyKeyboardMarkup(rows=rows, resize=resize, single_use=single_use, selective=selective, persistent=persistent, force_reply=force_reply, placeholder=placeholder)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.resize else 0
        flags |= (1 << 1) if self.single_use else 0
        flags |= (1 << 2) if self.selective else 0
        flags |= (1 << 4) if self.persistent else 0
        flags |= (1 << 5) if self.force_reply else 0
        flags |= (1 << 3) if self.placeholder is not None else 0
        b.write(Int(flags))
        
        b.write(Vector(self.rows))
        
        if self.placeholder is not None:
            b.write(String(self.placeholder))
        
        return b.getvalue()
