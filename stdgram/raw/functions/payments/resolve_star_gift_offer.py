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


class ResolveStarGiftOffer(TLObject["raw.base.Updates"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``E9CE781C``

    Parameters:
        offer_msg_id (``int`` ``32-bit``):
            N/A

        decline (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <stdgram.raw.base.Updates>`
    """

    __slots__: list[str] = ["offer_msg_id", "decline"]

    ID = 0xe9ce781c
    QUALNAME = "functions.payments.ResolveStarGiftOffer"

    def __init__(self, *, offer_msg_id: int, decline: bool | None = None) -> None:
        self.offer_msg_id = offer_msg_id  # int
        self.decline = decline  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> ResolveStarGiftOffer:
        
        flags = Int.read(b)
        
        decline = True if flags & (1 << 0) else False
        offer_msg_id = Int.read(b)
        
        return ResolveStarGiftOffer(offer_msg_id=offer_msg_id, decline=decline)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.decline else 0
        b.write(Int(flags))
        
        b.write(Int(self.offer_msg_id))
        
        return b.getvalue()
