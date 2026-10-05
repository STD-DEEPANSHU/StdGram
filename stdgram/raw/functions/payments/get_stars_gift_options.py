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


class GetStarsGiftOptions(TLObject["list[raw.base.StarsGiftOption]"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``D3C96BC8``

    Parameters:
        user_id (:obj:`InputUser <stdgram.raw.base.InputUser>`, *optional*):
            N/A

    Returns:
        List of :obj:`StarsGiftOption <stdgram.raw.base.StarsGiftOption>`
    """

    __slots__: list[str] = ["user_id"]

    ID = 0xd3c96bc8
    QUALNAME = "functions.payments.GetStarsGiftOptions"

    def __init__(self, *, user_id: raw.base.InputUser | None = None) -> None:
        self.user_id = user_id  # flags.0?InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GetStarsGiftOptions:
        
        flags = Int.read(b)
        
        user_id = TLObject.read(b) if flags & (1 << 0) else None
        
        return GetStarsGiftOptions(user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.user_id is not None else 0
        b.write(Int(flags))
        
        if self.user_id is not None:
            b.write(self.user_id.write())
        
        return b.getvalue()
