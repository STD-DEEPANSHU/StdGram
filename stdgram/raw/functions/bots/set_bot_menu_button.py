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


class SetBotMenuButton(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``4504D54F``

    Parameters:
        user_id (:obj:`InputUser <stdgram.raw.base.InputUser>`):
            N/A

        button (:obj:`BotMenuButton <stdgram.raw.base.BotMenuButton>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["user_id", "button"]

    ID = 0x4504d54f
    QUALNAME = "functions.bots.SetBotMenuButton"

    def __init__(self, *, user_id: raw.base.InputUser, button: raw.base.BotMenuButton) -> None:
        self.user_id = user_id  # InputUser
        self.button = button  # BotMenuButton

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SetBotMenuButton:
        # No flags
        
        user_id = TLObject.read(b)
        
        button = TLObject.read(b)
        
        return SetBotMenuButton(user_id=user_id, button=button)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.user_id.write())
        
        b.write(self.button.write())
        
        return b.getvalue()
