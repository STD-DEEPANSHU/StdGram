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


class FinishFirebasePnvLogin(TLObject["raw.base.auth.Authorization"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``2C85094C``

    Parameters:
        google_token (``str``):
            N/A

    Returns:
        :obj:`auth.Authorization <stdgram.raw.base.auth.Authorization>`
    """

    __slots__: list[str] = ["google_token"]

    ID = 0x2c85094c
    QUALNAME = "functions.auth.FinishFirebasePnvLogin"

    def __init__(self, *, google_token: str) -> None:
        self.google_token = google_token  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> FinishFirebasePnvLogin:
        # No flags
        
        google_token = String.read(b)
        
        return FinishFirebasePnvLogin(google_token=google_token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.google_token))
        
        return b.getvalue()
