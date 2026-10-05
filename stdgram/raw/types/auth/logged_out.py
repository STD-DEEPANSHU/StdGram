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


class LoggedOut(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.auth.LoggedOut`.

    Details:
        - Layer: ``229``
        - ID: ``C3A2835F``

    Parameters:
        future_auth_token (``bytes``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.LogOut
    """

    __slots__: list[str] = ["future_auth_token"]

    ID = 0xc3a2835f
    QUALNAME = "types.auth.LoggedOut"

    def __init__(self, *, future_auth_token: bytes | None = None) -> None:
        self.future_auth_token = future_auth_token  # flags.0?bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> LoggedOut:
        
        flags = Int.read(b)
        
        future_auth_token = Bytes.read(b) if flags & (1 << 0) else None
        return LoggedOut(future_auth_token=future_auth_token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.future_auth_token is not None else 0
        b.write(Int(flags))
        
        if self.future_auth_token is not None:
            b.write(Bytes(self.future_auth_token))
        
        return b.getvalue()
