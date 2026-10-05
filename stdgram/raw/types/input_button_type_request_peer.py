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


class InputButtonTypeRequestPeer(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.ButtonType`.

    Details:
        - Layer: ``229``
        - ID: ``3FE268FE``

    Parameters:
        button_id (``int`` ``32-bit``):
            N/A

        peer_type (:obj:`RequestPeerType <stdgram.raw.base.RequestPeerType>`):
            N/A

        max_quantity (``int`` ``32-bit``):
            N/A

        name_requested (``bool``, *optional*):
            N/A

        username_requested (``bool``, *optional*):
            N/A

        photo_requested (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["button_id", "peer_type", "max_quantity", "name_requested", "username_requested", "photo_requested"]

    ID = 0x3fe268fe
    QUALNAME = "types.InputButtonTypeRequestPeer"

    def __init__(self, *, button_id: int, peer_type: raw.base.RequestPeerType, max_quantity: int, name_requested: bool | None = None, username_requested: bool | None = None, photo_requested: bool | None = None) -> None:
        self.button_id = button_id  # int
        self.peer_type = peer_type  # RequestPeerType
        self.max_quantity = max_quantity  # int
        self.name_requested = name_requested  # flags.0?true
        self.username_requested = username_requested  # flags.1?true
        self.photo_requested = photo_requested  # flags.2?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputButtonTypeRequestPeer:
        
        flags = Int.read(b)
        
        name_requested = True if flags & (1 << 0) else False
        username_requested = True if flags & (1 << 1) else False
        photo_requested = True if flags & (1 << 2) else False
        button_id = Int.read(b)
        
        peer_type = TLObject.read(b)
        
        max_quantity = Int.read(b)
        
        return InputButtonTypeRequestPeer(button_id=button_id, peer_type=peer_type, max_quantity=max_quantity, name_requested=name_requested, username_requested=username_requested, photo_requested=photo_requested)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.name_requested else 0
        flags |= (1 << 1) if self.username_requested else 0
        flags |= (1 << 2) if self.photo_requested else 0
        b.write(Int(flags))
        
        b.write(Int(self.button_id))
        
        b.write(self.peer_type.write())
        
        b.write(Int(self.max_quantity))
        
        return b.getvalue()
