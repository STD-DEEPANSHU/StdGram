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


class ResaleStarGifts(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.payments.ResaleStarGifts`.

    Details:
        - Layer: ``229``
        - ID: ``947A12DF``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        gifts (List of :obj:`StarGift <stdgram.raw.base.StarGift>`):
            N/A

        chats (List of :obj:`Chat <stdgram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <stdgram.raw.base.User>`):
            N/A

        next_offset (``str``, *optional*):
            N/A

        attributes (List of :obj:`StarGiftAttribute <stdgram.raw.base.StarGiftAttribute>`, *optional*):
            N/A

        attributes_hash (``int`` ``64-bit``, *optional*):
            N/A

        counters (List of :obj:`StarGiftAttributeCounter <stdgram.raw.base.StarGiftAttributeCounter>`, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetResaleStarGifts
    """

    __slots__: list[str] = ["count", "gifts", "chats", "users", "next_offset", "attributes", "attributes_hash", "counters"]

    ID = 0x947a12df
    QUALNAME = "types.payments.ResaleStarGifts"

    def __init__(self, *, count: int, gifts: list[raw.base.StarGift], chats: list[raw.base.Chat], users: list[raw.base.User], next_offset: str | None = None, attributes: list[raw.base.StarGiftAttribute] | None = None, attributes_hash: int | None = None, counters: list[raw.base.StarGiftAttributeCounter] | None = None) -> None:
        self.count = count  # int
        self.gifts = gifts  # Vector<StarGift>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.next_offset = next_offset  # flags.0?string
        self.attributes = attributes  # flags.1?Vector<StarGiftAttribute>
        self.attributes_hash = attributes_hash  # flags.1?long
        self.counters = counters  # flags.2?Vector<StarGiftAttributeCounter>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> ResaleStarGifts:
        
        flags = Int.read(b)
        
        count = Int.read(b)
        
        gifts = TLObject.read(b)
        
        next_offset = String.read(b) if flags & (1 << 0) else None
        attributes = TLObject.read(b) if flags & (1 << 1) else []
        
        attributes_hash = Long.read(b) if flags & (1 << 1) else None
        chats = TLObject.read(b)
        
        counters = TLObject.read(b) if flags & (1 << 2) else []
        
        users = TLObject.read(b)
        
        return ResaleStarGifts(count=count, gifts=gifts, chats=chats, users=users, next_offset=next_offset, attributes=attributes, attributes_hash=attributes_hash, counters=counters)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        flags |= (1 << 1) if self.attributes else 0
        flags |= (1 << 1) if self.attributes_hash is not None else 0
        flags |= (1 << 2) if self.counters else 0
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        b.write(Vector(self.gifts))
        
        if self.next_offset is not None:
            b.write(String(self.next_offset))
        
        if self.attributes is not None:
            b.write(Vector(self.attributes))
        
        if self.attributes_hash is not None:
            b.write(Long(self.attributes_hash))
        
        b.write(Vector(self.chats))
        
        if self.counters is not None:
            b.write(Vector(self.counters))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
