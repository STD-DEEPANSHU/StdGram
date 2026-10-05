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


class ReplyInlineMarkup(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.ReplyMarkup`.

    Details:
        - Layer: ``229``
        - ID: ``B2B15770``

    Parameters:
        rows (List of :obj:`KeyboardInlineButtonRow <stdgram.raw.base.KeyboardInlineButtonRow>`):
            N/A

        force_reply (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["rows", "force_reply"]

    ID = 0xb2b15770
    QUALNAME = "types.ReplyInlineMarkup"

    def __init__(self, *, rows: list[raw.base.KeyboardInlineButtonRow], force_reply: bool | None = None) -> None:
        self.rows = rows  # Vector<KeyboardInlineButtonRow>
        self.force_reply = force_reply  # flags.5?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> ReplyInlineMarkup:
        
        flags = Int.read(b)
        
        force_reply = True if flags & (1 << 5) else False
        rows = TLObject.read(b)
        
        return ReplyInlineMarkup(rows=rows, force_reply=force_reply)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.force_reply else 0
        b.write(Int(flags))
        
        b.write(Vector(self.rows))
        
        return b.getvalue()
