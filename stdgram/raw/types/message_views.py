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


class MessageViews(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.MessageViews`.

    Details:
        - Layer: ``229``
        - ID: ``455B853D``

    Parameters:
        views (``int`` ``32-bit``, *optional*):
            N/A

        forwards (``int`` ``32-bit``, *optional*):
            N/A

        replies (:obj:`MessageReplies <stdgram.raw.base.MessageReplies>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["views", "forwards", "replies"]

    ID = 0x455b853d
    QUALNAME = "types.MessageViews"

    def __init__(self, *, views: int | None = None, forwards: int | None = None, replies: raw.base.MessageReplies | None = None) -> None:
        self.views = views  # flags.0?int
        self.forwards = forwards  # flags.1?int
        self.replies = replies  # flags.2?MessageReplies

    @staticmethod
    def read(b: BytesIO, *args: Any) -> MessageViews:
        
        flags = Int.read(b)
        
        views = Int.read(b) if flags & (1 << 0) else None
        forwards = Int.read(b) if flags & (1 << 1) else None
        replies = TLObject.read(b) if flags & (1 << 2) else None
        
        return MessageViews(views=views, forwards=forwards, replies=replies)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.views is not None else 0
        flags |= (1 << 1) if self.forwards is not None else 0
        flags |= (1 << 2) if self.replies is not None else 0
        b.write(Int(flags))
        
        if self.views is not None:
            b.write(Int(self.views))
        
        if self.forwards is not None:
            b.write(Int(self.forwards))
        
        if self.replies is not None:
            b.write(self.replies.write())
        
        return b.getvalue()
