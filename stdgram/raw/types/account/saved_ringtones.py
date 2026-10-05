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


class SavedRingtones(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.account.SavedRingtones`.

    Details:
        - Layer: ``229``
        - ID: ``C1E92CC5``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

        ringtones (List of :obj:`Document <stdgram.raw.base.Document>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetSavedRingtones
    """

    __slots__: list[str] = ["hash", "ringtones"]

    ID = 0xc1e92cc5
    QUALNAME = "types.account.SavedRingtones"

    def __init__(self, *, hash: int, ringtones: list[raw.base.Document]) -> None:
        self.hash = hash  # long
        self.ringtones = ringtones  # Vector<Document>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SavedRingtones:
        # No flags
        
        hash = Long.read(b)
        
        ringtones = TLObject.read(b)
        
        return SavedRingtones(hash=hash, ringtones=ringtones)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Vector(self.ringtones))
        
        return b.getvalue()
