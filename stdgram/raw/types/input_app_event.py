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


class InputAppEvent(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputAppEvent`.

    Details:
        - Layer: ``229``
        - ID: ``1D1B1245``

    Parameters:
        time (``float`` ``64-bit``):
            N/A

        type (``str``):
            N/A

        peer (``int`` ``64-bit``):
            N/A

        data (:obj:`JSONValue <stdgram.raw.base.JSONValue>`):
            N/A

    """

    __slots__: list[str] = ["time", "type", "peer", "data"]

    ID = 0x1d1b1245
    QUALNAME = "types.InputAppEvent"

    def __init__(self, *, time: float, type: str, peer: int, data: raw.base.JSONValue) -> None:
        self.time = time  # double
        self.type = type  # string
        self.peer = peer  # long
        self.data = data  # JSONValue

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputAppEvent:
        # No flags
        
        time = Double.read(b)
        
        type = String.read(b)
        
        peer = Long.read(b)
        
        data = TLObject.read(b)
        
        return InputAppEvent(time=time, type=type, peer=peer, data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Double(self.time))
        
        b.write(String(self.type))
        
        b.write(Long(self.peer))
        
        b.write(self.data.write())
        
        return b.getvalue()
