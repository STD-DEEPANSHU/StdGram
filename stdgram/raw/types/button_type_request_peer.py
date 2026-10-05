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


class ButtonTypeRequestPeer(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.ButtonType`.

    Details:
        - Layer: ``229``
        - ID: ``4F58A237``

    Parameters:
        button_id (``int`` ``32-bit``):
            N/A

        peer_type (:obj:`RequestPeerType <stdgram.raw.base.RequestPeerType>`):
            N/A

        max_quantity (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["button_id", "peer_type", "max_quantity"]

    ID = 0x4f58a237
    QUALNAME = "types.ButtonTypeRequestPeer"

    def __init__(self, *, button_id: int, peer_type: raw.base.RequestPeerType, max_quantity: int) -> None:
        self.button_id = button_id  # int
        self.peer_type = peer_type  # RequestPeerType
        self.max_quantity = max_quantity  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> ButtonTypeRequestPeer:
        
        flags = Int.read(b)
        
        button_id = Int.read(b)
        
        peer_type = TLObject.read(b)
        
        max_quantity = Int.read(b)
        
        return ButtonTypeRequestPeer(button_id=button_id, peer_type=peer_type, max_quantity=max_quantity)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Int(self.button_id))
        
        b.write(self.peer_type.write())
        
        b.write(Int(self.max_quantity))
        
        return b.getvalue()
