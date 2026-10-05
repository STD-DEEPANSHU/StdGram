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


class CheckCanSendGiftResultFail(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.payments.CheckCanSendGiftResult`.

    Details:
        - Layer: ``229``
        - ID: ``D5E58274``

    Parameters:
        reason (:obj:`TextWithEntities <stdgram.raw.base.TextWithEntities>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.CheckCanSendGift
    """

    __slots__: list[str] = ["reason"]

    ID = 0xd5e58274
    QUALNAME = "types.payments.CheckCanSendGiftResultFail"

    def __init__(self, *, reason: raw.base.TextWithEntities) -> None:
        self.reason = reason  # TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> CheckCanSendGiftResultFail:
        # No flags
        
        reason = TLObject.read(b)
        
        return CheckCanSendGiftResultFail(reason=reason)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.reason.write())
        
        return b.getvalue()
