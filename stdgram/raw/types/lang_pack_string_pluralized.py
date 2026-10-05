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


class LangPackStringPluralized(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.LangPackString`.

    Details:
        - Layer: ``229``
        - ID: ``6C47AC9F``

    Parameters:
        key (``str``):
            N/A

        other_value (``str``):
            N/A

        zero_value (``str``, *optional*):
            N/A

        one_value (``str``, *optional*):
            N/A

        two_value (``str``, *optional*):
            N/A

        few_value (``str``, *optional*):
            N/A

        many_value (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            langpack.GetStrings
    """

    __slots__: list[str] = ["key", "other_value", "zero_value", "one_value", "two_value", "few_value", "many_value"]

    ID = 0x6c47ac9f
    QUALNAME = "types.LangPackStringPluralized"

    def __init__(self, *, key: str, other_value: str, zero_value: str | None = None, one_value: str | None = None, two_value: str | None = None, few_value: str | None = None, many_value: str | None = None) -> None:
        self.key = key  # string
        self.other_value = other_value  # string
        self.zero_value = zero_value  # flags.0?string
        self.one_value = one_value  # flags.1?string
        self.two_value = two_value  # flags.2?string
        self.few_value = few_value  # flags.3?string
        self.many_value = many_value  # flags.4?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> LangPackStringPluralized:
        
        flags = Int.read(b)
        
        key = String.read(b)
        
        zero_value = String.read(b) if flags & (1 << 0) else None
        one_value = String.read(b) if flags & (1 << 1) else None
        two_value = String.read(b) if flags & (1 << 2) else None
        few_value = String.read(b) if flags & (1 << 3) else None
        many_value = String.read(b) if flags & (1 << 4) else None
        other_value = String.read(b)
        
        return LangPackStringPluralized(key=key, other_value=other_value, zero_value=zero_value, one_value=one_value, two_value=two_value, few_value=few_value, many_value=many_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.zero_value is not None else 0
        flags |= (1 << 1) if self.one_value is not None else 0
        flags |= (1 << 2) if self.two_value is not None else 0
        flags |= (1 << 3) if self.few_value is not None else 0
        flags |= (1 << 4) if self.many_value is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.key))
        
        if self.zero_value is not None:
            b.write(String(self.zero_value))
        
        if self.one_value is not None:
            b.write(String(self.one_value))
        
        if self.two_value is not None:
            b.write(String(self.two_value))
        
        if self.few_value is not None:
            b.write(String(self.few_value))
        
        if self.many_value is not None:
            b.write(String(self.many_value))
        
        b.write(String(self.other_value))
        
        return b.getvalue()
