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


class PopularContact(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.PopularContact`.

    Details:
        - Layer: ``229``
        - ID: ``5CE14175``

    Parameters:
        client_id (``int`` ``64-bit``):
            N/A

        importers (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["client_id", "importers"]

    ID = 0x5ce14175
    QUALNAME = "types.PopularContact"

    def __init__(self, *, client_id: int, importers: int) -> None:
        self.client_id = client_id  # long
        self.importers = importers  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> PopularContact:
        # No flags
        
        client_id = Long.read(b)
        
        importers = Int.read(b)
        
        return PopularContact(client_id=client_id, importers=importers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.client_id))
        
        b.write(Int(self.importers))
        
        return b.getvalue()
