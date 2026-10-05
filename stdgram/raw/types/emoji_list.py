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


class EmojiList(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.EmojiList`.

    Details:
        - Layer: ``229``
        - ID: ``7A1E11D1``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

        document_id (List of ``int`` ``64-bit``):
            N/A

    Functions:
        This object can be returned by 5 functions.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetDefaultProfilePhotoEmojis
            account.GetDefaultGroupPhotoEmojis
            account.GetDefaultBackgroundEmojis
            account.GetChannelRestrictedStatusEmojis
            messages.SearchCustomEmoji
    """

    __slots__: list[str] = ["hash", "document_id"]

    ID = 0x7a1e11d1
    QUALNAME = "types.EmojiList"

    def __init__(self, *, hash: int, document_id: list[int]) -> None:
        self.hash = hash  # long
        self.document_id = document_id  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> EmojiList:
        # No flags
        
        hash = Long.read(b)
        
        document_id = TLObject.read(b, Long)
        
        return EmojiList(hash=hash, document_id=document_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Vector(self.document_id, Long))
        
        return b.getvalue()
