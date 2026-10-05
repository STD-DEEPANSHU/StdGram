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


class UpdatePrivacy(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.Update`.

    Details:
        - Layer: ``229``
        - ID: ``EE3B272A``

    Parameters:
        key (:obj:`PrivacyKey <stdgram.raw.base.PrivacyKey>`):
            N/A

        rules (List of :obj:`PrivacyRule <stdgram.raw.base.PrivacyRule>`):
            N/A

    """

    __slots__: list[str] = ["key", "rules"]

    ID = 0xee3b272a
    QUALNAME = "types.UpdatePrivacy"

    def __init__(self, *, key: raw.base.PrivacyKey, rules: list[raw.base.PrivacyRule]) -> None:
        self.key = key  # PrivacyKey
        self.rules = rules  # Vector<PrivacyRule>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdatePrivacy:
        # No flags
        
        key = TLObject.read(b)
        
        rules = TLObject.read(b)
        
        return UpdatePrivacy(key=key, rules=rules)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.key.write())
        
        b.write(Vector(self.rules))
        
        return b.getvalue()
