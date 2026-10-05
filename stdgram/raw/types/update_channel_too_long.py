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


class UpdateChannelTooLong(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.Update`.

    Details:
        - Layer: ``229``
        - ID: ``108D941F``

    Parameters:
        channel_id (``int`` ``64-bit``):
            N/A

        pts (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: list[str] = ["channel_id", "pts"]

    ID = 0x108d941f
    QUALNAME = "types.UpdateChannelTooLong"

    def __init__(self, *, channel_id: int, pts: int | None = None) -> None:
        self.channel_id = channel_id  # long
        self.pts = pts  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateChannelTooLong:
        
        flags = Int.read(b)
        
        channel_id = Long.read(b)
        
        pts = Int.read(b) if flags & (1 << 0) else None
        return UpdateChannelTooLong(channel_id=channel_id, pts=pts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.pts is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.channel_id))
        
        if self.pts is not None:
            b.write(Int(self.pts))
        
        return b.getvalue()
