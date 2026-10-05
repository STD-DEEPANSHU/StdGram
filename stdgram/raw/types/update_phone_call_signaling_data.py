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


class UpdatePhoneCallSignalingData(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.Update`.

    Details:
        - Layer: ``229``
        - ID: ``2661BF09``

    Parameters:
        phone_call_id (``int`` ``64-bit``):
            N/A

        data (``bytes``):
            N/A

    """

    __slots__: list[str] = ["phone_call_id", "data"]

    ID = 0x2661bf09
    QUALNAME = "types.UpdatePhoneCallSignalingData"

    def __init__(self, *, phone_call_id: int, data: bytes) -> None:
        self.phone_call_id = phone_call_id  # long
        self.data = data  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdatePhoneCallSignalingData:
        # No flags
        
        phone_call_id = Long.read(b)
        
        data = Bytes.read(b)
        
        return UpdatePhoneCallSignalingData(phone_call_id=phone_call_id, data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.phone_call_id))
        
        b.write(Bytes(self.data))
        
        return b.getvalue()
