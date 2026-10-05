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


class MessageActionGroupCall(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.MessageAction`.

    Details:
        - Layer: ``229``
        - ID: ``7A0D7F42``

    Parameters:
        call (:obj:`InputGroupCall <stdgram.raw.base.InputGroupCall>`):
            N/A

        duration (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: list[str] = ["call", "duration"]

    ID = 0x7a0d7f42
    QUALNAME = "types.MessageActionGroupCall"

    def __init__(self, *, call: raw.base.InputGroupCall, duration: int | None = None) -> None:
        self.call = call  # InputGroupCall
        self.duration = duration  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> MessageActionGroupCall:
        
        flags = Int.read(b)
        
        call = TLObject.read(b)
        
        duration = Int.read(b) if flags & (1 << 0) else None
        return MessageActionGroupCall(call=call, duration=duration)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.duration is not None else 0
        b.write(Int(flags))
        
        b.write(self.call.write())
        
        if self.duration is not None:
            b.write(Int(self.duration))
        
        return b.getvalue()
