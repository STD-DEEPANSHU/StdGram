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


class GetPrivacy(TLObject["raw.base.account.PrivacyRules"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``DADBC950``

    Parameters:
        key (:obj:`InputPrivacyKey <stdgram.raw.base.InputPrivacyKey>`):
            N/A

    Returns:
        :obj:`account.PrivacyRules <stdgram.raw.base.account.PrivacyRules>`
    """

    __slots__: list[str] = ["key"]

    ID = 0xdadbc950
    QUALNAME = "functions.account.GetPrivacy"

    def __init__(self, *, key: raw.base.InputPrivacyKey) -> None:
        self.key = key  # InputPrivacyKey

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GetPrivacy:
        # No flags
        
        key = TLObject.read(b)
        
        return GetPrivacy(key=key)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.key.write())
        
        return b.getvalue()
