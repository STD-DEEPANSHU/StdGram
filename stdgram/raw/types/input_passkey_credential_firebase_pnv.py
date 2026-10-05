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


class InputPasskeyCredentialFirebasePNV(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputPasskeyCredential`.

    Details:
        - Layer: ``229``
        - ID: ``5B1CCB28``

    Parameters:
        pnv_token (``str``):
            N/A

    """

    __slots__: list[str] = ["pnv_token"]

    ID = 0x5b1ccb28
    QUALNAME = "types.InputPasskeyCredentialFirebasePNV"

    def __init__(self, *, pnv_token: str) -> None:
        self.pnv_token = pnv_token  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputPasskeyCredentialFirebasePNV:
        # No flags
        
        pnv_token = String.read(b)
        
        return InputPasskeyCredentialFirebasePNV(pnv_token=pnv_token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.pnv_token))
        
        return b.getvalue()
