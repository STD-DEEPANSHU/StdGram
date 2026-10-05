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


class PhoneCall(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.phone.PhoneCall`.

    Details:
        - Layer: ``229``
        - ID: ``EC82E140``

    Parameters:
        phone_call (:obj:`PhoneCall <stdgram.raw.base.PhoneCall>`):
            N/A

        users (List of :obj:`User <stdgram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            phone.RequestCall
            phone.AcceptCall
            phone.ConfirmCall
    """

    __slots__: list[str] = ["phone_call", "users"]

    ID = 0xec82e140
    QUALNAME = "types.phone.PhoneCall"

    def __init__(self, *, phone_call: raw.base.PhoneCall, users: list[raw.base.User]) -> None:
        self.phone_call = phone_call  # PhoneCall
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> PhoneCall:
        # No flags
        
        phone_call = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return PhoneCall(phone_call=phone_call, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.phone_call.write())
        
        b.write(Vector(self.users))
        
        return b.getvalue()
