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


class GetAuthorizationForm(TLObject["raw.base.account.AuthorizationForm"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``A929597A``

    Parameters:
        bot_id (``int`` ``64-bit``):
            N/A

        scope (``str``):
            N/A

        public_key (``str``):
            N/A

    Returns:
        :obj:`account.AuthorizationForm <stdgram.raw.base.account.AuthorizationForm>`
    """

    __slots__: list[str] = ["bot_id", "scope", "public_key"]

    ID = 0xa929597a
    QUALNAME = "functions.account.GetAuthorizationForm"

    def __init__(self, *, bot_id: int, scope: str, public_key: str) -> None:
        self.bot_id = bot_id  # long
        self.scope = scope  # string
        self.public_key = public_key  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GetAuthorizationForm:
        # No flags
        
        bot_id = Long.read(b)
        
        scope = String.read(b)
        
        public_key = String.read(b)
        
        return GetAuthorizationForm(bot_id=bot_id, scope=scope, public_key=public_key)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.bot_id))
        
        b.write(String(self.scope))
        
        b.write(String(self.public_key))
        
        return b.getvalue()
