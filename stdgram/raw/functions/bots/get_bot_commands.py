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


class GetBotCommands(TLObject["list[raw.base.BotCommand]"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``E34C0DD6``

    Parameters:
        scope (:obj:`BotCommandScope <stdgram.raw.base.BotCommandScope>`):
            N/A

        lang_code (``str``):
            N/A

    Returns:
        List of :obj:`BotCommand <stdgram.raw.base.BotCommand>`
    """

    __slots__: list[str] = ["scope", "lang_code"]

    ID = 0xe34c0dd6
    QUALNAME = "functions.bots.GetBotCommands"

    def __init__(self, *, scope: raw.base.BotCommandScope, lang_code: str) -> None:
        self.scope = scope  # BotCommandScope
        self.lang_code = lang_code  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GetBotCommands:
        # No flags
        
        scope = TLObject.read(b)
        
        lang_code = String.read(b)
        
        return GetBotCommands(scope=scope, lang_code=lang_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.scope.write())
        
        b.write(String(self.lang_code))
        
        return b.getvalue()
