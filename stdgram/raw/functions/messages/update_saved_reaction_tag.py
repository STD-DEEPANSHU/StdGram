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


class UpdateSavedReactionTag(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``60297DEC``

    Parameters:
        reaction (:obj:`Reaction <stdgram.raw.base.Reaction>`):
            N/A

        title (``str``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["reaction", "title"]

    ID = 0x60297dec
    QUALNAME = "functions.messages.UpdateSavedReactionTag"

    def __init__(self, *, reaction: raw.base.Reaction, title: str | None = None) -> None:
        self.reaction = reaction  # Reaction
        self.title = title  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateSavedReactionTag:
        
        flags = Int.read(b)
        
        reaction = TLObject.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        return UpdateSavedReactionTag(reaction=reaction, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.title is not None else 0
        b.write(Int(flags))
        
        b.write(self.reaction.write())
        
        if self.title is not None:
            b.write(String(self.title))
        
        return b.getvalue()
