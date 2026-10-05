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


class ContactBirthday(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.ContactBirthday`.

    Details:
        - Layer: ``229``
        - ID: ``1D998733``

    Parameters:
        contact_id (``int`` ``64-bit``):
            N/A

        birthday (:obj:`Birthday <stdgram.raw.base.Birthday>`):
            N/A

    """

    __slots__: list[str] = ["contact_id", "birthday"]

    ID = 0x1d998733
    QUALNAME = "types.ContactBirthday"

    def __init__(self, *, contact_id: int, birthday: raw.base.Birthday) -> None:
        self.contact_id = contact_id  # long
        self.birthday = birthday  # Birthday

    @staticmethod
    def read(b: BytesIO, *args: Any) -> ContactBirthday:
        # No flags
        
        contact_id = Long.read(b)
        
        birthday = TLObject.read(b)
        
        return ContactBirthday(contact_id=contact_id, birthday=birthday)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.contact_id))
        
        b.write(self.birthday.write())
        
        return b.getvalue()
