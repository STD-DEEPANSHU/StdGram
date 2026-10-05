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


class ExportBotToken(TLObject["raw.base.bots.ExportedBotToken"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``BD0D99EB``

    Parameters:
        bot (:obj:`InputUser <stdgram.raw.base.InputUser>`):
            N/A

        revoke (``bool``):
            N/A

    Returns:
        :obj:`bots.ExportedBotToken <stdgram.raw.base.bots.ExportedBotToken>`
    """

    __slots__: list[str] = ["bot", "revoke"]

    ID = 0xbd0d99eb
    QUALNAME = "functions.bots.ExportBotToken"

    def __init__(self, *, bot: raw.base.InputUser, revoke: bool) -> None:
        self.bot = bot  # InputUser
        self.revoke = revoke  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> ExportBotToken:
        # No flags
        
        bot = TLObject.read(b)
        
        revoke = Bool.read(b)
        
        return ExportBotToken(bot=bot, revoke=revoke)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot.write())
        
        b.write(Bool(self.revoke))
        
        return b.getvalue()
