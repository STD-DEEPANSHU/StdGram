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


class RestrictionReason(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.RestrictionReason`.

    Details:
        - Layer: ``229``
        - ID: ``D072ACB4``

    Parameters:
        platform (``str``):
            N/A

        reason (``str``):
            N/A

        text (``str``):
            N/A

    """

    __slots__: list[str] = ["platform", "reason", "text"]

    ID = 0xd072acb4
    QUALNAME = "types.RestrictionReason"

    def __init__(self, *, platform: str, reason: str, text: str) -> None:
        self.platform = platform  # string
        self.reason = reason  # string
        self.text = text  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> RestrictionReason:
        # No flags
        
        platform = String.read(b)
        
        reason = String.read(b)
        
        text = String.read(b)
        
        return RestrictionReason(platform=platform, reason=reason, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.platform))
        
        b.write(String(self.reason))
        
        b.write(String(self.text))
        
        return b.getvalue()
