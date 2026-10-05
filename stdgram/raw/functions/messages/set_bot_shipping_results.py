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


class SetBotShippingResults(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``E5F672FA``

    Parameters:
        query_id (``int`` ``64-bit``):
            N/A

        error (``str``, *optional*):
            N/A

        shipping_options (List of :obj:`ShippingOption <stdgram.raw.base.ShippingOption>`, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["query_id", "error", "shipping_options"]

    ID = 0xe5f672fa
    QUALNAME = "functions.messages.SetBotShippingResults"

    def __init__(self, *, query_id: int, error: str | None = None, shipping_options: list[raw.base.ShippingOption] | None = None) -> None:
        self.query_id = query_id  # long
        self.error = error  # flags.0?string
        self.shipping_options = shipping_options  # flags.1?Vector<ShippingOption>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SetBotShippingResults:
        
        flags = Int.read(b)
        
        query_id = Long.read(b)
        
        error = String.read(b) if flags & (1 << 0) else None
        shipping_options = TLObject.read(b) if flags & (1 << 1) else []
        
        return SetBotShippingResults(query_id=query_id, error=error, shipping_options=shipping_options)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.error is not None else 0
        flags |= (1 << 1) if self.shipping_options else 0
        b.write(Int(flags))
        
        b.write(Long(self.query_id))
        
        if self.error is not None:
            b.write(String(self.error))
        
        if self.shipping_options is not None:
            b.write(Vector(self.shipping_options))
        
        return b.getvalue()
