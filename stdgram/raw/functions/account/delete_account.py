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


class DeleteAccount(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``A2C0CF74``

    Parameters:
        reason (``str``):
            N/A

        password (:obj:`InputCheckPasswordSRP <stdgram.raw.base.InputCheckPasswordSRP>`, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["reason", "password"]

    ID = 0xa2c0cf74
    QUALNAME = "functions.account.DeleteAccount"

    def __init__(self, *, reason: str, password: raw.base.InputCheckPasswordSRP | None = None) -> None:
        self.reason = reason  # string
        self.password = password  # flags.0?InputCheckPasswordSRP

    @staticmethod
    def read(b: BytesIO, *args: Any) -> DeleteAccount:
        
        flags = Int.read(b)
        
        reason = String.read(b)
        
        password = TLObject.read(b) if flags & (1 << 0) else None
        
        return DeleteAccount(reason=reason, password=password)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.password is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.reason))
        
        if self.password is not None:
            b.write(self.password.write())
        
        return b.getvalue()
