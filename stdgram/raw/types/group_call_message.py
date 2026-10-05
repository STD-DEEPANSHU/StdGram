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


class GroupCallMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.GroupCallMessage`.

    Details:
        - Layer: ``229``
        - ID: ``1A8AFC7E``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        from_id (:obj:`Peer <stdgram.raw.base.Peer>`):
            N/A

        date (``int`` ``32-bit``):
            N/A

        message (:obj:`TextWithEntities <stdgram.raw.base.TextWithEntities>`):
            N/A

        from_admin (``bool``, *optional*):
            N/A

        paid_message_stars (``int`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: list[str] = ["id", "from_id", "date", "message", "from_admin", "paid_message_stars"]

    ID = 0x1a8afc7e
    QUALNAME = "types.GroupCallMessage"

    def __init__(self, *, id: int, from_id: raw.base.Peer, date: int, message: raw.base.TextWithEntities, from_admin: bool | None = None, paid_message_stars: int | None = None) -> None:
        self.id = id  # int
        self.from_id = from_id  # Peer
        self.date = date  # int
        self.message = message  # TextWithEntities
        self.from_admin = from_admin  # flags.1?true
        self.paid_message_stars = paid_message_stars  # flags.0?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GroupCallMessage:
        
        flags = Int.read(b)
        
        from_admin = True if flags & (1 << 1) else False
        id = Int.read(b)
        
        from_id = TLObject.read(b)
        
        date = Int.read(b)
        
        message = TLObject.read(b)
        
        paid_message_stars = Long.read(b) if flags & (1 << 0) else None
        return GroupCallMessage(id=id, from_id=from_id, date=date, message=message, from_admin=from_admin, paid_message_stars=paid_message_stars)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.from_admin else 0
        flags |= (1 << 0) if self.paid_message_stars is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(self.from_id.write())
        
        b.write(Int(self.date))
        
        b.write(self.message.write())
        
        if self.paid_message_stars is not None:
            b.write(Long(self.paid_message_stars))
        
        return b.getvalue()
