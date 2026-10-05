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


class SetBotGuestChatResult(TLObject["raw.base.InputBotInlineMessageID"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``B8F106E3``

    Parameters:
        query_id (``int`` ``64-bit``):
            N/A

        result (:obj:`InputBotInlineResult <stdgram.raw.base.InputBotInlineResult>`):
            N/A

    Returns:
        :obj:`InputBotInlineMessageID <stdgram.raw.base.InputBotInlineMessageID>`
    """

    __slots__: list[str] = ["query_id", "result"]

    ID = 0xb8f106e3
    QUALNAME = "functions.messages.SetBotGuestChatResult"

    def __init__(self, *, query_id: int, result: raw.base.InputBotInlineResult) -> None:
        self.query_id = query_id  # long
        self.result = result  # InputBotInlineResult

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SetBotGuestChatResult:
        # No flags
        
        query_id = Long.read(b)
        
        result = TLObject.read(b)
        
        return SetBotGuestChatResult(query_id=query_id, result=result)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.query_id))
        
        b.write(self.result.write())
        
        return b.getvalue()
