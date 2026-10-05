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


class UpdateBotGuestChatQuery(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.Update`.

    Details:
        - Layer: ``229``
        - ID: ``CDD4093D``

    Parameters:
        query_id (``int`` ``64-bit``):
            N/A

        message (:obj:`Message <stdgram.raw.base.Message>`):
            N/A

        qts (``int`` ``32-bit``):
            N/A

        reference_messages (List of :obj:`Message <stdgram.raw.base.Message>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["query_id", "message", "qts", "reference_messages"]

    ID = 0xcdd4093d
    QUALNAME = "types.UpdateBotGuestChatQuery"

    def __init__(self, *, query_id: int, message: raw.base.Message, qts: int, reference_messages: list[raw.base.Message] | None = None) -> None:
        self.query_id = query_id  # long
        self.message = message  # Message
        self.qts = qts  # int
        self.reference_messages = reference_messages  # flags.0?Vector<Message>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateBotGuestChatQuery:
        
        flags = Int.read(b)
        
        query_id = Long.read(b)
        
        message = TLObject.read(b)
        
        reference_messages = TLObject.read(b) if flags & (1 << 0) else []
        
        qts = Int.read(b)
        
        return UpdateBotGuestChatQuery(query_id=query_id, message=message, qts=qts, reference_messages=reference_messages)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.reference_messages else 0
        b.write(Int(flags))
        
        b.write(Long(self.query_id))
        
        b.write(self.message.write())
        
        if self.reference_messages is not None:
            b.write(Vector(self.reference_messages))
        
        b.write(Int(self.qts))
        
        return b.getvalue()
