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


class ToggleNoPaidMessagesException(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``FE2EDA76``

    Parameters:
        user_id (:obj:`InputUser <stdgram.raw.base.InputUser>`):
            N/A

        refund_charged (``bool``, *optional*):
            N/A

        require_payment (``bool``, *optional*):
            N/A

        parent_peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["user_id", "refund_charged", "require_payment", "parent_peer"]

    ID = 0xfe2eda76
    QUALNAME = "functions.account.ToggleNoPaidMessagesException"

    def __init__(self, *, user_id: raw.base.InputUser, refund_charged: bool | None = None, require_payment: bool | None = None, parent_peer: raw.base.InputPeer | None = None) -> None:
        self.user_id = user_id  # InputUser
        self.refund_charged = refund_charged  # flags.0?true
        self.require_payment = require_payment  # flags.2?true
        self.parent_peer = parent_peer  # flags.1?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> ToggleNoPaidMessagesException:
        
        flags = Int.read(b)
        
        refund_charged = True if flags & (1 << 0) else False
        require_payment = True if flags & (1 << 2) else False
        parent_peer = TLObject.read(b) if flags & (1 << 1) else None
        
        user_id = TLObject.read(b)
        
        return ToggleNoPaidMessagesException(user_id=user_id, refund_charged=refund_charged, require_payment=require_payment, parent_peer=parent_peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.refund_charged else 0
        flags |= (1 << 2) if self.require_payment else 0
        flags |= (1 << 1) if self.parent_peer is not None else 0
        b.write(Int(flags))
        
        if self.parent_peer is not None:
            b.write(self.parent_peer.write())
        
        b.write(self.user_id.write())
        
        return b.getvalue()
