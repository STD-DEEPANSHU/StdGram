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


class MsgDetailedInfo(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.MsgDetailedInfo`.

    Details:
        - Layer: ``229``
        - ID: ``276D3EC6``

    Parameters:
        msg_id (``int`` ``64-bit``):
            N/A

        answer_msg_id (``int`` ``64-bit``):
            N/A

        bytes (``int`` ``32-bit``):
            N/A

        status (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["msg_id", "answer_msg_id", "bytes", "status"]

    ID = 0x276d3ec6
    QUALNAME = "types.MsgDetailedInfo"

    def __init__(self, *, msg_id: int, answer_msg_id: int, bytes: int, status: int) -> None:
        self.msg_id = msg_id  # long
        self.answer_msg_id = answer_msg_id  # long
        self.bytes = bytes  # int
        self.status = status  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> MsgDetailedInfo:
        # No flags
        
        msg_id = Long.read(b)
        
        answer_msg_id = Long.read(b)
        
        bytes = Int.read(b)
        
        status = Int.read(b)
        
        return MsgDetailedInfo(msg_id=msg_id, answer_msg_id=answer_msg_id, bytes=bytes, status=status)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.msg_id))
        
        b.write(Long(self.answer_msg_id))
        
        b.write(Int(self.bytes))
        
        b.write(Int(self.status))
        
        return b.getvalue()
