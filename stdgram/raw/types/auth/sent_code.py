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


class SentCode(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.auth.SentCode`.

    Details:
        - Layer: ``229``
        - ID: ``5E002502``

    Parameters:
        type (:obj:`auth.SentCodeType <stdgram.raw.base.auth.SentCodeType>`):
            N/A

        phone_code_hash (``str``):
            N/A

        next_type (:obj:`auth.CodeType <stdgram.raw.base.auth.CodeType>`, *optional*):
            N/A

        timeout (``int`` ``32-bit``, *optional*):
            N/A

    Functions:
        This object can be returned by 7 functions.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.SendCode
            auth.ResendCode
            auth.ResetLoginEmail
            auth.CheckPaidAuth
            account.SendChangePhoneCode
            account.SendConfirmPhoneCode
            account.SendVerifyPhoneCode
    """

    __slots__: list[str] = ["type", "phone_code_hash", "next_type", "timeout"]

    ID = 0x5e002502
    QUALNAME = "types.auth.SentCode"

    def __init__(self, *, type: raw.base.auth.SentCodeType, phone_code_hash: str, next_type: raw.base.auth.CodeType | None = None, timeout: int | None = None) -> None:
        self.type = type  # auth.SentCodeType
        self.phone_code_hash = phone_code_hash  # string
        self.next_type = next_type  # flags.1?auth.CodeType
        self.timeout = timeout  # flags.2?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SentCode:
        
        flags = Int.read(b)
        
        type = TLObject.read(b)
        
        phone_code_hash = String.read(b)
        
        next_type = TLObject.read(b) if flags & (1 << 1) else None
        
        timeout = Int.read(b) if flags & (1 << 2) else None
        return SentCode(type=type, phone_code_hash=phone_code_hash, next_type=next_type, timeout=timeout)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.next_type is not None else 0
        flags |= (1 << 2) if self.timeout is not None else 0
        b.write(Int(flags))
        
        b.write(self.type.write())
        
        b.write(String(self.phone_code_hash))
        
        if self.next_type is not None:
            b.write(self.next_type.write())
        
        if self.timeout is not None:
            b.write(Int(self.timeout))
        
        return b.getvalue()
