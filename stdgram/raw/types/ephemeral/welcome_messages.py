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


class WelcomeMessages(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.ephemeral.WelcomeMessages`.

    Details:
        - Layer: ``229``
        - ID: ``104FC872``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

        messages (List of :obj:`EphemeralMessage <stdgram.raw.base.EphemeralMessage>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            ephemeral.GetWelcomeMessages
    """

    __slots__: list[str] = ["hash", "messages"]

    ID = 0x104fc872
    QUALNAME = "types.ephemeral.WelcomeMessages"

    def __init__(self, *, hash: int, messages: list[raw.base.EphemeralMessage]) -> None:
        self.hash = hash  # long
        self.messages = messages  # Vector<EphemeralMessage>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> WelcomeMessages:
        # No flags
        
        hash = Long.read(b)
        
        messages = TLObject.read(b)
        
        return WelcomeMessages(hash=hash, messages=messages)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Vector(self.messages))
        
        return b.getvalue()
