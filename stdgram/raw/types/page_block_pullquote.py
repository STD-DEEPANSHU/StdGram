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


class PageBlockPullquote(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.PageBlock`.

    Details:
        - Layer: ``229``
        - ID: ``4F4456D3``

    Parameters:
        text (:obj:`RichText <stdgram.raw.base.RichText>`):
            N/A

        caption (:obj:`RichText <stdgram.raw.base.RichText>`):
            N/A

    """

    __slots__: list[str] = ["text", "caption"]

    ID = 0x4f4456d3
    QUALNAME = "types.PageBlockPullquote"

    def __init__(self, *, text: raw.base.RichText, caption: raw.base.RichText) -> None:
        self.text = text  # RichText
        self.caption = caption  # RichText

    @staticmethod
    def read(b: BytesIO, *args: Any) -> PageBlockPullquote:
        # No flags
        
        text = TLObject.read(b)
        
        caption = TLObject.read(b)
        
        return PageBlockPullquote(text=text, caption=caption)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.text.write())
        
        b.write(self.caption.write())
        
        return b.getvalue()
