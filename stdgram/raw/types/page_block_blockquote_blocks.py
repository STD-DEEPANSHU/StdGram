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


class PageBlockBlockquoteBlocks(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.PageBlock`.

    Details:
        - Layer: ``229``
        - ID: ``E6E47C4``

    Parameters:
        blocks (List of :obj:`PageBlock <stdgram.raw.base.PageBlock>`):
            N/A

        caption (:obj:`RichText <stdgram.raw.base.RichText>`):
            N/A

    """

    __slots__: list[str] = ["blocks", "caption"]

    ID = 0xe6e47c4
    QUALNAME = "types.PageBlockBlockquoteBlocks"

    def __init__(self, *, blocks: list[raw.base.PageBlock], caption: raw.base.RichText) -> None:
        self.blocks = blocks  # Vector<PageBlock>
        self.caption = caption  # RichText

    @staticmethod
    def read(b: BytesIO, *args: Any) -> PageBlockBlockquoteBlocks:
        # No flags
        
        blocks = TLObject.read(b)
        
        caption = TLObject.read(b)
        
        return PageBlockBlockquoteBlocks(blocks=blocks, caption=caption)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.blocks))
        
        b.write(self.caption.write())
        
        return b.getvalue()
