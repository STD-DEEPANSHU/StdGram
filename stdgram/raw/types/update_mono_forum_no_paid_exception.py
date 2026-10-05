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


class UpdateMonoForumNoPaidException(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.Update`.

    Details:
        - Layer: ``229``
        - ID: ``9F812B08``

    Parameters:
        channel_id (``int`` ``64-bit``):
            N/A

        saved_peer_id (:obj:`Peer <stdgram.raw.base.Peer>`):
            N/A

        exception (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["channel_id", "saved_peer_id", "exception"]

    ID = 0x9f812b08
    QUALNAME = "types.UpdateMonoForumNoPaidException"

    def __init__(self, *, channel_id: int, saved_peer_id: raw.base.Peer, exception: bool | None = None) -> None:
        self.channel_id = channel_id  # long
        self.saved_peer_id = saved_peer_id  # Peer
        self.exception = exception  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateMonoForumNoPaidException:
        
        flags = Int.read(b)
        
        exception = True if flags & (1 << 0) else False
        channel_id = Long.read(b)
        
        saved_peer_id = TLObject.read(b)
        
        return UpdateMonoForumNoPaidException(channel_id=channel_id, saved_peer_id=saved_peer_id, exception=exception)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.exception else 0
        b.write(Int(flags))
        
        b.write(Long(self.channel_id))
        
        b.write(self.saved_peer_id.write())
        
        return b.getvalue()
