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


class SetBotCallbackAnswer(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``D58F130A``

    Parameters:
        query_id (``int`` ``64-bit``):
            N/A

        cache_time (``int`` ``32-bit``):
            N/A

        alert (``bool``, *optional*):
            N/A

        message (``str``, *optional*):
            N/A

        url (``str``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["query_id", "cache_time", "alert", "message", "url"]

    ID = 0xd58f130a
    QUALNAME = "functions.messages.SetBotCallbackAnswer"

    def __init__(self, *, query_id: int, cache_time: int, alert: bool | None = None, message: str | None = None, url: str | None = None) -> None:
        self.query_id = query_id  # long
        self.cache_time = cache_time  # int
        self.alert = alert  # flags.1?true
        self.message = message  # flags.0?string
        self.url = url  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SetBotCallbackAnswer:
        
        flags = Int.read(b)
        
        alert = True if flags & (1 << 1) else False
        query_id = Long.read(b)
        
        message = String.read(b) if flags & (1 << 0) else None
        url = String.read(b) if flags & (1 << 2) else None
        cache_time = Int.read(b)
        
        return SetBotCallbackAnswer(query_id=query_id, cache_time=cache_time, alert=alert, message=message, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.alert else 0
        flags |= (1 << 0) if self.message is not None else 0
        flags |= (1 << 2) if self.url is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.query_id))
        
        if self.message is not None:
            b.write(String(self.message))
        
        if self.url is not None:
            b.write(String(self.url))
        
        b.write(Int(self.cache_time))
        
        return b.getvalue()
