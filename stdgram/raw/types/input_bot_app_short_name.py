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


class InputBotAppShortName(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputBotApp`.

    Details:
        - Layer: ``229``
        - ID: ``908C0407``

    Parameters:
        bot_id (:obj:`InputUser <stdgram.raw.base.InputUser>`):
            N/A

        short_name (``str``):
            N/A

    """

    __slots__: list[str] = ["bot_id", "short_name"]

    ID = 0x908c0407
    QUALNAME = "types.InputBotAppShortName"

    def __init__(self, *, bot_id: raw.base.InputUser, short_name: str) -> None:
        self.bot_id = bot_id  # InputUser
        self.short_name = short_name  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputBotAppShortName:
        # No flags
        
        bot_id = TLObject.read(b)
        
        short_name = String.read(b)
        
        return InputBotAppShortName(bot_id=bot_id, short_name=short_name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot_id.write())
        
        b.write(String(self.short_name))
        
        return b.getvalue()
