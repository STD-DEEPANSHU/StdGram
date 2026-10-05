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


class FirebasePnvSignUp(TLObject["raw.base.auth.Authorization"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``783F6B56``

    Parameters:
        first_name (``str``):
            N/A

        last_name (``str``):
            N/A

        no_joined_notifications (``bool``, *optional*):
            N/A

    Returns:
        :obj:`auth.Authorization <stdgram.raw.base.auth.Authorization>`
    """

    __slots__: list[str] = ["first_name", "last_name", "no_joined_notifications"]

    ID = 0x783f6b56
    QUALNAME = "functions.auth.FirebasePnvSignUp"

    def __init__(self, *, first_name: str, last_name: str, no_joined_notifications: bool | None = None) -> None:
        self.first_name = first_name  # string
        self.last_name = last_name  # string
        self.no_joined_notifications = no_joined_notifications  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> FirebasePnvSignUp:
        
        flags = Int.read(b)
        
        no_joined_notifications = True if flags & (1 << 0) else False
        first_name = String.read(b)
        
        last_name = String.read(b)
        
        return FirebasePnvSignUp(first_name=first_name, last_name=last_name, no_joined_notifications=no_joined_notifications)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.no_joined_notifications else 0
        b.write(Int(flags))
        
        b.write(String(self.first_name))
        
        b.write(String(self.last_name))
        
        return b.getvalue()
