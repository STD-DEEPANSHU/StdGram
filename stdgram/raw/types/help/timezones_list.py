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


class TimezonesList(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.help.TimezonesList`.

    Details:
        - Layer: ``229``
        - ID: ``7B74ED71``

    Parameters:
        timezones (List of :obj:`Timezone <stdgram.raw.base.Timezone>`):
            N/A

        hash (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetTimezonesList
    """

    __slots__: list[str] = ["timezones", "hash"]

    ID = 0x7b74ed71
    QUALNAME = "types.help.TimezonesList"

    def __init__(self, *, timezones: list[raw.base.Timezone], hash: int) -> None:
        self.timezones = timezones  # Vector<Timezone>
        self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> TimezonesList:
        # No flags
        
        timezones = TLObject.read(b)
        
        hash = Int.read(b)
        
        return TimezonesList(timezones=timezones, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.timezones))
        
        b.write(Int(self.hash))
        
        return b.getvalue()
