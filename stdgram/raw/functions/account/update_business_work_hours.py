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


class UpdateBusinessWorkHours(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``4B00E066``

    Parameters:
        business_work_hours (:obj:`BusinessWorkHours <stdgram.raw.base.BusinessWorkHours>`, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["business_work_hours"]

    ID = 0x4b00e066
    QUALNAME = "functions.account.UpdateBusinessWorkHours"

    def __init__(self, *, business_work_hours: raw.base.BusinessWorkHours | None = None) -> None:
        self.business_work_hours = business_work_hours  # flags.0?BusinessWorkHours

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateBusinessWorkHours:
        
        flags = Int.read(b)
        
        business_work_hours = TLObject.read(b) if flags & (1 << 0) else None
        
        return UpdateBusinessWorkHours(business_work_hours=business_work_hours)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.business_work_hours is not None else 0
        b.write(Int(flags))
        
        if self.business_work_hours is not None:
            b.write(self.business_work_hours.write())
        
        return b.getvalue()
