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


class UpdateStarGiftCollection(TLObject["raw.base.StarGiftCollection"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``4FDDBEE7``

    Parameters:
        peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        collection_id (``int`` ``32-bit``):
            N/A

        title (``str``, *optional*):
            N/A

        delete_stargift (List of :obj:`InputSavedStarGift <stdgram.raw.base.InputSavedStarGift>`, *optional*):
            N/A

        add_stargift (List of :obj:`InputSavedStarGift <stdgram.raw.base.InputSavedStarGift>`, *optional*):
            N/A

        order (List of :obj:`InputSavedStarGift <stdgram.raw.base.InputSavedStarGift>`, *optional*):
            N/A

    Returns:
        :obj:`StarGiftCollection <stdgram.raw.base.StarGiftCollection>`
    """

    __slots__: list[str] = ["peer", "collection_id", "title", "delete_stargift", "add_stargift", "order"]

    ID = 0x4fddbee7
    QUALNAME = "functions.payments.UpdateStarGiftCollection"

    def __init__(self, *, peer: raw.base.InputPeer, collection_id: int, title: str | None = None, delete_stargift: list[raw.base.InputSavedStarGift] | None = None, add_stargift: list[raw.base.InputSavedStarGift] | None = None, order: list[raw.base.InputSavedStarGift] | None = None) -> None:
        self.peer = peer  # InputPeer
        self.collection_id = collection_id  # int
        self.title = title  # flags.0?string
        self.delete_stargift = delete_stargift  # flags.1?Vector<InputSavedStarGift>
        self.add_stargift = add_stargift  # flags.2?Vector<InputSavedStarGift>
        self.order = order  # flags.3?Vector<InputSavedStarGift>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateStarGiftCollection:
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        collection_id = Int.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        delete_stargift = TLObject.read(b) if flags & (1 << 1) else []
        
        add_stargift = TLObject.read(b) if flags & (1 << 2) else []
        
        order = TLObject.read(b) if flags & (1 << 3) else []
        
        return UpdateStarGiftCollection(peer=peer, collection_id=collection_id, title=title, delete_stargift=delete_stargift, add_stargift=add_stargift, order=order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.title is not None else 0
        flags |= (1 << 1) if self.delete_stargift else 0
        flags |= (1 << 2) if self.add_stargift else 0
        flags |= (1 << 3) if self.order else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.collection_id))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.delete_stargift is not None:
            b.write(Vector(self.delete_stargift))
        
        if self.add_stargift is not None:
            b.write(Vector(self.add_stargift))
        
        if self.order is not None:
            b.write(Vector(self.order))
        
        return b.getvalue()
