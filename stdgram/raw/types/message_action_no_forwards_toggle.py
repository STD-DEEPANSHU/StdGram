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


class MessageActionNoForwardsToggle(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.MessageAction`.

    Details:
        - Layer: ``229``
        - ID: ``BF7D6572``

    Parameters:
        prev_value (``bool``):
            N/A

        new_value (``bool``):
            N/A

    """

    __slots__: list[str] = ["prev_value", "new_value"]

    ID = 0xbf7d6572
    QUALNAME = "types.MessageActionNoForwardsToggle"

    def __init__(self, *, prev_value: bool, new_value: bool) -> None:
        self.prev_value = prev_value  # Bool
        self.new_value = new_value  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> MessageActionNoForwardsToggle:
        # No flags
        
        prev_value = Bool.read(b)
        
        new_value = Bool.read(b)
        
        return MessageActionNoForwardsToggle(prev_value=prev_value, new_value=new_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bool(self.prev_value))
        
        b.write(Bool(self.new_value))
        
        return b.getvalue()
