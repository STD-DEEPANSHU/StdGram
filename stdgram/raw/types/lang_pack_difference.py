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


class LangPackDifference(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.LangPackDifference`.

    Details:
        - Layer: ``229``
        - ID: ``F385C1F6``

    Parameters:
        lang_code (``str``):
            N/A

        from_version (``int`` ``32-bit``):
            N/A

        version (``int`` ``32-bit``):
            N/A

        strings (List of :obj:`LangPackString <stdgram.raw.base.LangPackString>`):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            langpack.GetLangPack
            langpack.GetDifference
    """

    __slots__: list[str] = ["lang_code", "from_version", "version", "strings"]

    ID = 0xf385c1f6
    QUALNAME = "types.LangPackDifference"

    def __init__(self, *, lang_code: str, from_version: int, version: int, strings: list[raw.base.LangPackString]) -> None:
        self.lang_code = lang_code  # string
        self.from_version = from_version  # int
        self.version = version  # int
        self.strings = strings  # Vector<LangPackString>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> LangPackDifference:
        # No flags
        
        lang_code = String.read(b)
        
        from_version = Int.read(b)
        
        version = Int.read(b)
        
        strings = TLObject.read(b)
        
        return LangPackDifference(lang_code=lang_code, from_version=from_version, version=version, strings=strings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.lang_code))
        
        b.write(Int(self.from_version))
        
        b.write(Int(self.version))
        
        b.write(Vector(self.strings))
        
        return b.getvalue()
