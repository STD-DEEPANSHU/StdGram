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


class StarsSubscription(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.StarsSubscription`.

    Details:
        - Layer: ``229``
        - ID: ``2E6EAB1A``

    Parameters:
        id (``str``):
            N/A

        peer (:obj:`Peer <stdgram.raw.base.Peer>`):
            N/A

        until_date (``int`` ``32-bit``):
            N/A

        pricing (:obj:`StarsSubscriptionPricing <stdgram.raw.base.StarsSubscriptionPricing>`):
            N/A

        canceled (``bool``, *optional*):
            N/A

        can_refulfill (``bool``, *optional*):
            N/A

        missing_balance (``bool``, *optional*):
            N/A

        bot_canceled (``bool``, *optional*):
            N/A

        chat_invite_hash (``str``, *optional*):
            N/A

        title (``str``, *optional*):
            N/A

        photo (:obj:`WebDocument <stdgram.raw.base.WebDocument>`, *optional*):
            N/A

        invoice_slug (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["id", "peer", "until_date", "pricing", "canceled", "can_refulfill", "missing_balance", "bot_canceled", "chat_invite_hash", "title", "photo", "invoice_slug"]

    ID = 0x2e6eab1a
    QUALNAME = "types.StarsSubscription"

    def __init__(self, *, id: str, peer: raw.base.Peer, until_date: int, pricing: raw.base.StarsSubscriptionPricing, canceled: bool | None = None, can_refulfill: bool | None = None, missing_balance: bool | None = None, bot_canceled: bool | None = None, chat_invite_hash: str | None = None, title: str | None = None, photo: raw.base.WebDocument | None = None, invoice_slug: str | None = None) -> None:
        self.id = id  # string
        self.peer = peer  # Peer
        self.until_date = until_date  # int
        self.pricing = pricing  # StarsSubscriptionPricing
        self.canceled = canceled  # flags.0?true
        self.can_refulfill = can_refulfill  # flags.1?true
        self.missing_balance = missing_balance  # flags.2?true
        self.bot_canceled = bot_canceled  # flags.7?true
        self.chat_invite_hash = chat_invite_hash  # flags.3?string
        self.title = title  # flags.4?string
        self.photo = photo  # flags.5?WebDocument
        self.invoice_slug = invoice_slug  # flags.6?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> StarsSubscription:
        
        flags = Int.read(b)
        
        canceled = True if flags & (1 << 0) else False
        can_refulfill = True if flags & (1 << 1) else False
        missing_balance = True if flags & (1 << 2) else False
        bot_canceled = True if flags & (1 << 7) else False
        id = String.read(b)
        
        peer = TLObject.read(b)
        
        until_date = Int.read(b)
        
        pricing = TLObject.read(b)
        
        chat_invite_hash = String.read(b) if flags & (1 << 3) else None
        title = String.read(b) if flags & (1 << 4) else None
        photo = TLObject.read(b) if flags & (1 << 5) else None
        
        invoice_slug = String.read(b) if flags & (1 << 6) else None
        return StarsSubscription(id=id, peer=peer, until_date=until_date, pricing=pricing, canceled=canceled, can_refulfill=can_refulfill, missing_balance=missing_balance, bot_canceled=bot_canceled, chat_invite_hash=chat_invite_hash, title=title, photo=photo, invoice_slug=invoice_slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.canceled else 0
        flags |= (1 << 1) if self.can_refulfill else 0
        flags |= (1 << 2) if self.missing_balance else 0
        flags |= (1 << 7) if self.bot_canceled else 0
        flags |= (1 << 3) if self.chat_invite_hash is not None else 0
        flags |= (1 << 4) if self.title is not None else 0
        flags |= (1 << 5) if self.photo is not None else 0
        flags |= (1 << 6) if self.invoice_slug is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.id))
        
        b.write(self.peer.write())
        
        b.write(Int(self.until_date))
        
        b.write(self.pricing.write())
        
        if self.chat_invite_hash is not None:
            b.write(String(self.chat_invite_hash))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        if self.invoice_slug is not None:
            b.write(String(self.invoice_slug))
        
        return b.getvalue()
