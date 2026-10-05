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


class InputBusinessIntro(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputBusinessIntro`.

    Details:
        - Layer: ``229``
        - ID: ``9C469CD``

    Parameters:
        title (``str``):
            N/A

        description (``str``):
            N/A

        sticker (:obj:`InputDocument <stdgram.raw.base.InputDocument>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["title", "description", "sticker"]

    ID = 0x9c469cd
    QUALNAME = "types.InputBusinessIntro"

    def __init__(self, *, title: str, description: str, sticker: raw.base.InputDocument | None = None) -> None:
        self.title = title  # string
        self.description = description  # string
        self.sticker = sticker  # flags.0?InputDocument

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputBusinessIntro:
        
        flags = Int.read(b)
        
        title = String.read(b)
        
        description = String.read(b)
        
        sticker = TLObject.read(b) if flags & (1 << 0) else None
        
        return InputBusinessIntro(title=title, description=description, sticker=sticker)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.sticker is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        if self.sticker is not None:
            b.write(self.sticker.write())
        
        return b.getvalue()
