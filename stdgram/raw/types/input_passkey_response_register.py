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


class InputPasskeyResponseRegister(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputPasskeyResponse`.

    Details:
        - Layer: ``229``
        - ID: ``3E63935C``

    Parameters:
        client_data (:obj:`DataJSON <stdgram.raw.base.DataJSON>`):
            N/A

        attestation_data (``bytes``):
            N/A

    """

    __slots__: list[str] = ["client_data", "attestation_data"]

    ID = 0x3e63935c
    QUALNAME = "types.InputPasskeyResponseRegister"

    def __init__(self, *, client_data: raw.base.DataJSON, attestation_data: bytes) -> None:
        self.client_data = client_data  # DataJSON
        self.attestation_data = attestation_data  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputPasskeyResponseRegister:
        # No flags
        
        client_data = TLObject.read(b)
        
        attestation_data = Bytes.read(b)
        
        return InputPasskeyResponseRegister(client_data=client_data, attestation_data=attestation_data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.client_data.write())
        
        b.write(Bytes(self.attestation_data))
        
        return b.getvalue()
