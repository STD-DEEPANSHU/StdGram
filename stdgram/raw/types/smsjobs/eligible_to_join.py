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


class EligibleToJoin(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.smsjobs.EligibilityToJoin`.

    Details:
        - Layer: ``229``
        - ID: ``DC8B44CF``

    Parameters:
        terms_url (``str``):
            N/A

        monthly_sent_sms (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            smsjobs.IsEligibleToJoin
    """

    __slots__: list[str] = ["terms_url", "monthly_sent_sms"]

    ID = 0xdc8b44cf
    QUALNAME = "types.smsjobs.EligibleToJoin"

    def __init__(self, *, terms_url: str, monthly_sent_sms: int) -> None:
        self.terms_url = terms_url  # string
        self.monthly_sent_sms = monthly_sent_sms  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> EligibleToJoin:
        # No flags
        
        terms_url = String.read(b)
        
        monthly_sent_sms = Int.read(b)
        
        return EligibleToJoin(terms_url=terms_url, monthly_sent_sms=monthly_sent_sms)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.terms_url))
        
        b.write(Int(self.monthly_sent_sms))
        
        return b.getvalue()
