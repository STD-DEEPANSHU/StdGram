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


class MessageEntityBlockquote(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.MessageEntity`.

    Details:
        - Layer: ``229``
        - ID: ``F1CCAAAC``

    Parameters:
        offset (``int`` ``32-bit``):
            N/A

        length (``int`` ``32-bit``):
            N/A

        collapsed (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["offset", "length", "collapsed"]

    ID = 0xf1ccaaac
    QUALNAME = "types.MessageEntityBlockquote"

    def __init__(self, *, offset: int, length: int, collapsed: bool | None = None) -> None:
        self.offset = offset  # int
        self.length = length  # int
        self.collapsed = collapsed  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> MessageEntityBlockquote:
        
        flags = Int.read(b)
        
        collapsed = True if flags & (1 << 0) else False
        offset = Int.read(b)
        
        length = Int.read(b)
        
        return MessageEntityBlockquote(offset=offset, length=length, collapsed=collapsed)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.collapsed else 0
        b.write(Int(flags))
        
        b.write(Int(self.offset))
        
        b.write(Int(self.length))
        
        return b.getvalue()
