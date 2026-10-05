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


class JsonObjectValue(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.JSONObjectValue`.

    Details:
        - Layer: ``229``
        - ID: ``C0DE1BD9``

    Parameters:
        key (``str``):
            N/A

        value (:obj:`JSONValue <stdgram.raw.base.JSONValue>`):
            N/A

    """

    __slots__: list[str] = ["key", "value"]

    ID = 0xc0de1bd9
    QUALNAME = "types.JsonObjectValue"

    def __init__(self, *, key: str, value: raw.base.JSONValue) -> None:
        self.key = key  # string
        self.value = value  # JSONValue

    @staticmethod
    def read(b: BytesIO, *args: Any) -> JsonObjectValue:
        # No flags
        
        key = String.read(b)
        
        value = TLObject.read(b)
        
        return JsonObjectValue(key=key, value=value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.key))
        
        b.write(self.value.write())
        
        return b.getvalue()
