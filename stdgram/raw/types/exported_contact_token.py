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


class ExportedContactToken(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.ExportedContactToken`.

    Details:
        - Layer: ``229``
        - ID: ``41BF109B``

    Parameters:
        url (``str``):
            N/A

        expires (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.ExportContactToken
    """

    __slots__: list[str] = ["url", "expires"]

    ID = 0x41bf109b
    QUALNAME = "types.ExportedContactToken"

    def __init__(self, *, url: str, expires: int) -> None:
        self.url = url  # string
        self.expires = expires  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> ExportedContactToken:
        # No flags
        
        url = String.read(b)
        
        expires = Int.read(b)
        
        return ExportedContactToken(url=url, expires=expires)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        b.write(Int(self.expires))
        
        return b.getvalue()
