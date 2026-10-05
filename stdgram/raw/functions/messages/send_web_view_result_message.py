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


class SendWebViewResultMessage(TLObject["raw.base.WebViewMessageSent"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``A4314F5``

    Parameters:
        bot_query_id (``str``):
            N/A

        result (:obj:`InputBotInlineResult <stdgram.raw.base.InputBotInlineResult>`):
            N/A

    Returns:
        :obj:`WebViewMessageSent <stdgram.raw.base.WebViewMessageSent>`
    """

    __slots__: list[str] = ["bot_query_id", "result"]

    ID = 0xa4314f5
    QUALNAME = "functions.messages.SendWebViewResultMessage"

    def __init__(self, *, bot_query_id: str, result: raw.base.InputBotInlineResult) -> None:
        self.bot_query_id = bot_query_id  # string
        self.result = result  # InputBotInlineResult

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SendWebViewResultMessage:
        # No flags
        
        bot_query_id = String.read(b)
        
        result = TLObject.read(b)
        
        return SendWebViewResultMessage(bot_query_id=bot_query_id, result=result)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.bot_query_id))
        
        b.write(self.result.write())
        
        return b.getvalue()
