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


class InlineButtonTypeUrlAuth(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InlineButtonType`.

    Details:
        - Layer: ``229``
        - ID: ``BFD02DA2``

    Parameters:
        url (``str``):
            N/A

        button_id (``int`` ``32-bit``):
            N/A

        fwd_text (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["url", "button_id", "fwd_text"]

    ID = 0xbfd02da2
    QUALNAME = "types.InlineButtonTypeUrlAuth"

    def __init__(self, *, url: str, button_id: int, fwd_text: str | None = None) -> None:
        self.url = url  # string
        self.button_id = button_id  # int
        self.fwd_text = fwd_text  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InlineButtonTypeUrlAuth:
        
        flags = Int.read(b)
        
        fwd_text = String.read(b) if flags & (1 << 0) else None
        url = String.read(b)
        
        button_id = Int.read(b)
        
        return InlineButtonTypeUrlAuth(url=url, button_id=button_id, fwd_text=fwd_text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.fwd_text is not None else 0
        b.write(Int(flags))
        
        if self.fwd_text is not None:
            b.write(String(self.fwd_text))
        
        b.write(String(self.url))
        
        b.write(Int(self.button_id))
        
        return b.getvalue()
