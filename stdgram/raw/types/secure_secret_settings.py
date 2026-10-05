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


class SecureSecretSettings(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.SecureSecretSettings`.

    Details:
        - Layer: ``229``
        - ID: ``1527BCAC``

    Parameters:
        secure_algo (:obj:`SecurePasswordKdfAlgo <stdgram.raw.base.SecurePasswordKdfAlgo>`):
            N/A

        secure_secret (``bytes``):
            N/A

        secure_secret_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: list[str] = ["secure_algo", "secure_secret", "secure_secret_id"]

    ID = 0x1527bcac
    QUALNAME = "types.SecureSecretSettings"

    def __init__(self, *, secure_algo: raw.base.SecurePasswordKdfAlgo, secure_secret: bytes, secure_secret_id: int) -> None:
        self.secure_algo = secure_algo  # SecurePasswordKdfAlgo
        self.secure_secret = secure_secret  # bytes
        self.secure_secret_id = secure_secret_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SecureSecretSettings:
        # No flags
        
        secure_algo = TLObject.read(b)
        
        secure_secret = Bytes.read(b)
        
        secure_secret_id = Long.read(b)
        
        return SecureSecretSettings(secure_algo=secure_algo, secure_secret=secure_secret, secure_secret_id=secure_secret_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.secure_algo.write())
        
        b.write(Bytes(self.secure_secret))
        
        b.write(Long(self.secure_secret_id))
        
        return b.getvalue()
