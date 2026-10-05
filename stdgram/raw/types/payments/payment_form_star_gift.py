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


class PaymentFormStarGift(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.payments.PaymentForm`.

    Details:
        - Layer: ``229``
        - ID: ``B425CFE1``

    Parameters:
        form_id (``int`` ``64-bit``):
            N/A

        invoice (:obj:`Invoice <stdgram.raw.base.Invoice>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetPaymentForm
    """

    __slots__: list[str] = ["form_id", "invoice"]

    ID = 0xb425cfe1
    QUALNAME = "types.payments.PaymentFormStarGift"

    def __init__(self, *, form_id: int, invoice: raw.base.Invoice) -> None:
        self.form_id = form_id  # long
        self.invoice = invoice  # Invoice

    @staticmethod
    def read(b: BytesIO, *args: Any) -> PaymentFormStarGift:
        # No flags
        
        form_id = Long.read(b)
        
        invoice = TLObject.read(b)
        
        return PaymentFormStarGift(form_id=form_id, invoice=invoice)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.form_id))
        
        b.write(self.invoice.write())
        
        return b.getvalue()
