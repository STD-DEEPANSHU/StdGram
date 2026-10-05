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


class PaymentRequestedInfo(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.PaymentRequestedInfo`.

    Details:
        - Layer: ``229``
        - ID: ``909C3F94``

    Parameters:
        name (``str``, *optional*):
            N/A

        phone (``str``, *optional*):
            N/A

        email (``str``, *optional*):
            N/A

        shipping_address (:obj:`PostAddress <stdgram.raw.base.PostAddress>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["name", "phone", "email", "shipping_address"]

    ID = 0x909c3f94
    QUALNAME = "types.PaymentRequestedInfo"

    def __init__(self, *, name: str | None = None, phone: str | None = None, email: str | None = None, shipping_address: raw.base.PostAddress | None = None) -> None:
        self.name = name  # flags.0?string
        self.phone = phone  # flags.1?string
        self.email = email  # flags.2?string
        self.shipping_address = shipping_address  # flags.3?PostAddress

    @staticmethod
    def read(b: BytesIO, *args: Any) -> PaymentRequestedInfo:
        
        flags = Int.read(b)
        
        name = String.read(b) if flags & (1 << 0) else None
        phone = String.read(b) if flags & (1 << 1) else None
        email = String.read(b) if flags & (1 << 2) else None
        shipping_address = TLObject.read(b) if flags & (1 << 3) else None
        
        return PaymentRequestedInfo(name=name, phone=phone, email=email, shipping_address=shipping_address)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.name is not None else 0
        flags |= (1 << 1) if self.phone is not None else 0
        flags |= (1 << 2) if self.email is not None else 0
        flags |= (1 << 3) if self.shipping_address is not None else 0
        b.write(Int(flags))
        
        if self.name is not None:
            b.write(String(self.name))
        
        if self.phone is not None:
            b.write(String(self.phone))
        
        if self.email is not None:
            b.write(String(self.email))
        
        if self.shipping_address is not None:
            b.write(self.shipping_address.write())
        
        return b.getvalue()
