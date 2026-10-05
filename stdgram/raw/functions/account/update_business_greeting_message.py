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


class UpdateBusinessGreetingMessage(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``66CDAFC4``

    Parameters:
        message (:obj:`InputBusinessGreetingMessage <stdgram.raw.base.InputBusinessGreetingMessage>`, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["message"]

    ID = 0x66cdafc4
    QUALNAME = "functions.account.UpdateBusinessGreetingMessage"

    def __init__(self, *, message: raw.base.InputBusinessGreetingMessage | None = None) -> None:
        self.message = message  # flags.0?InputBusinessGreetingMessage

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateBusinessGreetingMessage:
        
        flags = Int.read(b)
        
        message = TLObject.read(b) if flags & (1 << 0) else None
        
        return UpdateBusinessGreetingMessage(message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.message is not None else 0
        b.write(Int(flags))
        
        if self.message is not None:
            b.write(self.message.write())
        
        return b.getvalue()
