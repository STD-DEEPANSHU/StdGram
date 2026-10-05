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


class StarGiftUpgradeAttributes(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.payments.StarGiftUpgradeAttributes`.

    Details:
        - Layer: ``229``
        - ID: ``46C6E36F``

    Parameters:
        attributes (List of :obj:`StarGiftAttribute <stdgram.raw.base.StarGiftAttribute>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetStarGiftUpgradeAttributes
    """

    __slots__: list[str] = ["attributes"]

    ID = 0x46c6e36f
    QUALNAME = "types.payments.StarGiftUpgradeAttributes"

    def __init__(self, *, attributes: list[raw.base.StarGiftAttribute]) -> None:
        self.attributes = attributes  # Vector<StarGiftAttribute>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> StarGiftUpgradeAttributes:
        # No flags
        
        attributes = TLObject.read(b)
        
        return StarGiftUpgradeAttributes(attributes=attributes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.attributes))
        
        return b.getvalue()
