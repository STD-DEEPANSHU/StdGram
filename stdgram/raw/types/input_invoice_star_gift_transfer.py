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


class InputInvoiceStarGiftTransfer(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputInvoice`.

    Details:
        - Layer: ``229``
        - ID: ``4A5F5BD9``

    Parameters:
        stargift (:obj:`InputSavedStarGift <stdgram.raw.base.InputSavedStarGift>`):
            N/A

        to_id (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

    """

    __slots__: list[str] = ["stargift", "to_id"]

    ID = 0x4a5f5bd9
    QUALNAME = "types.InputInvoiceStarGiftTransfer"

    def __init__(self, *, stargift: raw.base.InputSavedStarGift, to_id: raw.base.InputPeer) -> None:
        self.stargift = stargift  # InputSavedStarGift
        self.to_id = to_id  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputInvoiceStarGiftTransfer:
        # No flags
        
        stargift = TLObject.read(b)
        
        to_id = TLObject.read(b)
        
        return InputInvoiceStarGiftTransfer(stargift=stargift, to_id=to_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.stargift.write())
        
        b.write(self.to_id.write())
        
        return b.getvalue()
