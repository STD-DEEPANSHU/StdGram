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


class Passkeys(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.account.Passkeys`.

    Details:
        - Layer: ``229``
        - ID: ``F8E0AA1C``

    Parameters:
        passkeys (List of :obj:`Passkey <stdgram.raw.base.Passkey>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetPasskeys
    """

    __slots__: list[str] = ["passkeys"]

    ID = 0xf8e0aa1c
    QUALNAME = "types.account.Passkeys"

    def __init__(self, *, passkeys: list[raw.base.Passkey]) -> None:
        self.passkeys = passkeys  # Vector<Passkey>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> Passkeys:
        # No flags
        
        passkeys = TLObject.read(b)
        
        return Passkeys(passkeys=passkeys)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.passkeys))
        
        return b.getvalue()
