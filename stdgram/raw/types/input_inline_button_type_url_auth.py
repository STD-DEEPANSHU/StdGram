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


class InputInlineButtonTypeUrlAuth(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InlineButtonType`.

    Details:
        - Layer: ``229``
        - ID: ``9961BCB4``

    Parameters:
        url (``str``):
            N/A

        request_write_access (``bool``, *optional*):
            N/A

        fwd_text (``str``, *optional*):
            N/A

        bot (:obj:`InputUser <stdgram.raw.base.InputUser>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["url", "request_write_access", "fwd_text", "bot"]

    ID = 0x9961bcb4
    QUALNAME = "types.InputInlineButtonTypeUrlAuth"

    def __init__(self, *, url: str, request_write_access: bool | None = None, fwd_text: str | None = None, bot: raw.base.InputUser | None = None) -> None:
        self.url = url  # string
        self.request_write_access = request_write_access  # flags.0?true
        self.fwd_text = fwd_text  # flags.1?string
        self.bot = bot  # flags.2?InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputInlineButtonTypeUrlAuth:
        
        flags = Int.read(b)
        
        request_write_access = True if flags & (1 << 0) else False
        fwd_text = String.read(b) if flags & (1 << 1) else None
        url = String.read(b)
        
        bot = TLObject.read(b) if flags & (1 << 2) else None
        
        return InputInlineButtonTypeUrlAuth(url=url, request_write_access=request_write_access, fwd_text=fwd_text, bot=bot)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.request_write_access else 0
        flags |= (1 << 1) if self.fwd_text is not None else 0
        flags |= (1 << 2) if self.bot is not None else 0
        b.write(Int(flags))
        
        if self.fwd_text is not None:
            b.write(String(self.fwd_text))
        
        b.write(String(self.url))
        
        if self.bot is not None:
            b.write(self.bot.write())
        
        return b.getvalue()
