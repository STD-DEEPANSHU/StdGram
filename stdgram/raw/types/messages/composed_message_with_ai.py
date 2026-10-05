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


class ComposedMessageWithAI(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.messages.ComposedMessageWithAI`.

    Details:
        - Layer: ``229``
        - ID: ``90D7ADFA``

    Parameters:
        result_text (:obj:`TextWithEntities <stdgram.raw.base.TextWithEntities>`):
            N/A

        diff_text (:obj:`TextWithEntities <stdgram.raw.base.TextWithEntities>`, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.ComposeMessageWithAI
    """

    __slots__: list[str] = ["result_text", "diff_text"]

    ID = 0x90d7adfa
    QUALNAME = "types.messages.ComposedMessageWithAI"

    def __init__(self, *, result_text: raw.base.TextWithEntities, diff_text: raw.base.TextWithEntities | None = None) -> None:
        self.result_text = result_text  # TextWithEntities
        self.diff_text = diff_text  # flags.0?TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> ComposedMessageWithAI:
        
        flags = Int.read(b)
        
        result_text = TLObject.read(b)
        
        diff_text = TLObject.read(b) if flags & (1 << 0) else None
        
        return ComposedMessageWithAI(result_text=result_text, diff_text=diff_text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.diff_text is not None else 0
        b.write(Int(flags))
        
        b.write(self.result_text.write())
        
        if self.diff_text is not None:
            b.write(self.diff_text.write())
        
        return b.getvalue()
