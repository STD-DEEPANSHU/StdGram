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


class FirebasePnvIntent(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.auth.FirebasePnvIntent`.

    Details:
        - Layer: ``229``
        - ID: ``DF5AC00C``

    Parameters:
        nonce (``str``):
            N/A

        digital_credential_payload (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.InitFirebasePnvLogin
    """

    __slots__: list[str] = ["nonce", "digital_credential_payload"]

    ID = 0xdf5ac00c
    QUALNAME = "types.auth.FirebasePnvIntent"

    def __init__(self, *, nonce: str, digital_credential_payload: str) -> None:
        self.nonce = nonce  # string
        self.digital_credential_payload = digital_credential_payload  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> FirebasePnvIntent:
        # No flags
        
        nonce = String.read(b)
        
        digital_credential_payload = String.read(b)
        
        return FirebasePnvIntent(nonce=nonce, digital_credential_payload=digital_credential_payload)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.nonce))
        
        b.write(String(self.digital_credential_payload))
        
        return b.getvalue()
