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


class SavedMusic(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.users.SavedMusic`.

    Details:
        - Layer: ``229``
        - ID: ``34A2F297``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        documents (List of :obj:`Document <stdgram.raw.base.Document>`):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            users.GetSavedMusic
            users.GetSavedMusicByID
    """

    __slots__: list[str] = ["count", "documents"]

    ID = 0x34a2f297
    QUALNAME = "types.users.SavedMusic"

    def __init__(self, *, count: int, documents: list[raw.base.Document]) -> None:
        self.count = count  # int
        self.documents = documents  # Vector<Document>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SavedMusic:
        # No flags
        
        count = Int.read(b)
        
        documents = TLObject.read(b)
        
        return SavedMusic(count=count, documents=documents)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.count))
        
        b.write(Vector(self.documents))
        
        return b.getvalue()
