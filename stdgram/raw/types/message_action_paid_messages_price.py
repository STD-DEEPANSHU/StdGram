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


class MessageActionPaidMessagesPrice(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.MessageAction`.

    Details:
        - Layer: ``229``
        - ID: ``84B88578``

    Parameters:
        stars (``int`` ``64-bit``):
            N/A

        broadcast_messages_allowed (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["stars", "broadcast_messages_allowed"]

    ID = 0x84b88578
    QUALNAME = "types.MessageActionPaidMessagesPrice"

    def __init__(self, *, stars: int, broadcast_messages_allowed: bool | None = None) -> None:
        self.stars = stars  # long
        self.broadcast_messages_allowed = broadcast_messages_allowed  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> MessageActionPaidMessagesPrice:
        
        flags = Int.read(b)
        
        broadcast_messages_allowed = True if flags & (1 << 0) else False
        stars = Long.read(b)
        
        return MessageActionPaidMessagesPrice(stars=stars, broadcast_messages_allowed=broadcast_messages_allowed)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.broadcast_messages_allowed else 0
        b.write(Int(flags))
        
        b.write(Long(self.stars))
        
        return b.getvalue()
