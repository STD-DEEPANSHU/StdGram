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


class MessageActionStarGiftUnique(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.MessageAction`.

    Details:
        - Layer: ``229``
        - ID: ``7E1C1187``

    Parameters:
        gift (:obj:`StarGift <stdgram.raw.base.StarGift>`):
            N/A

        upgrade (``bool``, *optional*):
            N/A

        transferred (``bool``, *optional*):
            N/A

        saved (``bool``, *optional*):
            N/A

        refunded (``bool``, *optional*):
            N/A

        prepaid_upgrade (``bool``, *optional*):
            N/A

        assigned (``bool``, *optional*):
            N/A

        from_offer (``bool``, *optional*):
            N/A

        craft (``bool``, *optional*):
            N/A

        name_hidden (``bool``, *optional*):
            N/A

        can_export_at (``int`` ``32-bit``, *optional*):
            N/A

        transfer_stars (``int`` ``64-bit``, *optional*):
            N/A

        from_id (:obj:`Peer <stdgram.raw.base.Peer>`, *optional*):
            N/A

        peer (:obj:`Peer <stdgram.raw.base.Peer>`, *optional*):
            N/A

        saved_id (``int`` ``64-bit``, *optional*):
            N/A

        resale_amount (:obj:`StarsAmount <stdgram.raw.base.StarsAmount>`, *optional*):
            N/A

        can_transfer_at (``int`` ``32-bit``, *optional*):
            N/A

        can_resell_at (``int`` ``32-bit``, *optional*):
            N/A

        drop_original_details_stars (``int`` ``64-bit``, *optional*):
            N/A

        can_craft_at (``int`` ``32-bit``, *optional*):
            N/A

        message (:obj:`TextWithEntities <stdgram.raw.base.TextWithEntities>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["gift", "upgrade", "transferred", "saved", "refunded", "prepaid_upgrade", "assigned", "from_offer", "craft", "name_hidden", "can_export_at", "transfer_stars", "from_id", "peer", "saved_id", "resale_amount", "can_transfer_at", "can_resell_at", "drop_original_details_stars", "can_craft_at", "message"]

    ID = 0x7e1c1187
    QUALNAME = "types.MessageActionStarGiftUnique"

    def __init__(self, *, gift: raw.base.StarGift, upgrade: bool | None = None, transferred: bool | None = None, saved: bool | None = None, refunded: bool | None = None, prepaid_upgrade: bool | None = None, assigned: bool | None = None, from_offer: bool | None = None, craft: bool | None = None, name_hidden: bool | None = None, can_export_at: int | None = None, transfer_stars: int | None = None, from_id: raw.base.Peer | None = None, peer: raw.base.Peer | None = None, saved_id: int | None = None, resale_amount: raw.base.StarsAmount | None = None, can_transfer_at: int | None = None, can_resell_at: int | None = None, drop_original_details_stars: int | None = None, can_craft_at: int | None = None, message: raw.base.TextWithEntities | None = None) -> None:
        self.gift = gift  # StarGift
        self.upgrade = upgrade  # flags.0?true
        self.transferred = transferred  # flags.1?true
        self.saved = saved  # flags.2?true
        self.refunded = refunded  # flags.5?true
        self.prepaid_upgrade = prepaid_upgrade  # flags.11?true
        self.assigned = assigned  # flags.13?true
        self.from_offer = from_offer  # flags.14?true
        self.craft = craft  # flags.16?true
        self.name_hidden = name_hidden  # flags.17?true
        self.can_export_at = can_export_at  # flags.3?int
        self.transfer_stars = transfer_stars  # flags.4?long
        self.from_id = from_id  # flags.6?Peer
        self.peer = peer  # flags.7?Peer
        self.saved_id = saved_id  # flags.7?long
        self.resale_amount = resale_amount  # flags.8?StarsAmount
        self.can_transfer_at = can_transfer_at  # flags.9?int
        self.can_resell_at = can_resell_at  # flags.10?int
        self.drop_original_details_stars = drop_original_details_stars  # flags.12?long
        self.can_craft_at = can_craft_at  # flags.15?int
        self.message = message  # flags.18?TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> MessageActionStarGiftUnique:
        
        flags = Int.read(b)
        
        upgrade = True if flags & (1 << 0) else False
        transferred = True if flags & (1 << 1) else False
        saved = True if flags & (1 << 2) else False
        refunded = True if flags & (1 << 5) else False
        prepaid_upgrade = True if flags & (1 << 11) else False
        assigned = True if flags & (1 << 13) else False
        from_offer = True if flags & (1 << 14) else False
        craft = True if flags & (1 << 16) else False
        name_hidden = True if flags & (1 << 17) else False
        gift = TLObject.read(b)
        
        can_export_at = Int.read(b) if flags & (1 << 3) else None
        transfer_stars = Long.read(b) if flags & (1 << 4) else None
        from_id = TLObject.read(b) if flags & (1 << 6) else None
        
        peer = TLObject.read(b) if flags & (1 << 7) else None
        
        saved_id = Long.read(b) if flags & (1 << 7) else None
        resale_amount = TLObject.read(b) if flags & (1 << 8) else None
        
        can_transfer_at = Int.read(b) if flags & (1 << 9) else None
        can_resell_at = Int.read(b) if flags & (1 << 10) else None
        drop_original_details_stars = Long.read(b) if flags & (1 << 12) else None
        can_craft_at = Int.read(b) if flags & (1 << 15) else None
        message = TLObject.read(b) if flags & (1 << 18) else None
        
        return MessageActionStarGiftUnique(gift=gift, upgrade=upgrade, transferred=transferred, saved=saved, refunded=refunded, prepaid_upgrade=prepaid_upgrade, assigned=assigned, from_offer=from_offer, craft=craft, name_hidden=name_hidden, can_export_at=can_export_at, transfer_stars=transfer_stars, from_id=from_id, peer=peer, saved_id=saved_id, resale_amount=resale_amount, can_transfer_at=can_transfer_at, can_resell_at=can_resell_at, drop_original_details_stars=drop_original_details_stars, can_craft_at=can_craft_at, message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.upgrade else 0
        flags |= (1 << 1) if self.transferred else 0
        flags |= (1 << 2) if self.saved else 0
        flags |= (1 << 5) if self.refunded else 0
        flags |= (1 << 11) if self.prepaid_upgrade else 0
        flags |= (1 << 13) if self.assigned else 0
        flags |= (1 << 14) if self.from_offer else 0
        flags |= (1 << 16) if self.craft else 0
        flags |= (1 << 17) if self.name_hidden else 0
        flags |= (1 << 3) if self.can_export_at is not None else 0
        flags |= (1 << 4) if self.transfer_stars is not None else 0
        flags |= (1 << 6) if self.from_id is not None else 0
        flags |= (1 << 7) if self.peer is not None else 0
        flags |= (1 << 7) if self.saved_id is not None else 0
        flags |= (1 << 8) if self.resale_amount is not None else 0
        flags |= (1 << 9) if self.can_transfer_at is not None else 0
        flags |= (1 << 10) if self.can_resell_at is not None else 0
        flags |= (1 << 12) if self.drop_original_details_stars is not None else 0
        flags |= (1 << 15) if self.can_craft_at is not None else 0
        flags |= (1 << 18) if self.message is not None else 0
        b.write(Int(flags))
        
        b.write(self.gift.write())
        
        if self.can_export_at is not None:
            b.write(Int(self.can_export_at))
        
        if self.transfer_stars is not None:
            b.write(Long(self.transfer_stars))
        
        if self.from_id is not None:
            b.write(self.from_id.write())
        
        if self.peer is not None:
            b.write(self.peer.write())
        
        if self.saved_id is not None:
            b.write(Long(self.saved_id))
        
        if self.resale_amount is not None:
            b.write(self.resale_amount.write())
        
        if self.can_transfer_at is not None:
            b.write(Int(self.can_transfer_at))
        
        if self.can_resell_at is not None:
            b.write(Int(self.can_resell_at))
        
        if self.drop_original_details_stars is not None:
            b.write(Long(self.drop_original_details_stars))
        
        if self.can_craft_at is not None:
            b.write(Int(self.can_craft_at))
        
        if self.message is not None:
            b.write(self.message.write())
        
        return b.getvalue()
