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


class MessageMediaInvoice(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.MessageMedia`.

    Details:
        - Layer: ``229``
        - ID: ``F6A548D3``

    Parameters:
        title (``str``):
            N/A

        description (``str``):
            N/A

        currency (``str``):
            N/A

        total_amount (``int`` ``64-bit``):
            N/A

        start_param (``str``):
            N/A

        shipping_address_requested (``bool``, *optional*):
            N/A

        test (``bool``, *optional*):
            N/A

        photo (:obj:`WebDocument <stdgram.raw.base.WebDocument>`, *optional*):
            N/A

        receipt_msg_id (``int`` ``32-bit``, *optional*):
            N/A

        extended_media (:obj:`MessageExtendedMedia <stdgram.raw.base.MessageExtendedMedia>`, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: list[str] = ["title", "description", "currency", "total_amount", "start_param", "shipping_address_requested", "test", "photo", "receipt_msg_id", "extended_media"]

    ID = 0xf6a548d3
    QUALNAME = "types.MessageMediaInvoice"

    def __init__(self, *, title: str, description: str, currency: str, total_amount: int, start_param: str, shipping_address_requested: bool | None = None, test: bool | None = None, photo: raw.base.WebDocument | None = None, receipt_msg_id: int | None = None, extended_media: raw.base.MessageExtendedMedia | None = None) -> None:
        self.title = title  # string
        self.description = description  # string
        self.currency = currency  # string
        self.total_amount = total_amount  # long
        self.start_param = start_param  # string
        self.shipping_address_requested = shipping_address_requested  # flags.1?true
        self.test = test  # flags.3?true
        self.photo = photo  # flags.0?WebDocument
        self.receipt_msg_id = receipt_msg_id  # flags.2?int
        self.extended_media = extended_media  # flags.4?MessageExtendedMedia

    @staticmethod
    def read(b: BytesIO, *args: Any) -> MessageMediaInvoice:
        
        flags = Int.read(b)
        
        shipping_address_requested = True if flags & (1 << 1) else False
        test = True if flags & (1 << 3) else False
        title = String.read(b)
        
        description = String.read(b)
        
        photo = TLObject.read(b) if flags & (1 << 0) else None
        
        receipt_msg_id = Int.read(b) if flags & (1 << 2) else None
        currency = String.read(b)
        
        total_amount = Long.read(b)
        
        start_param = String.read(b)
        
        extended_media = TLObject.read(b) if flags & (1 << 4) else None
        
        return MessageMediaInvoice(title=title, description=description, currency=currency, total_amount=total_amount, start_param=start_param, shipping_address_requested=shipping_address_requested, test=test, photo=photo, receipt_msg_id=receipt_msg_id, extended_media=extended_media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.shipping_address_requested else 0
        flags |= (1 << 3) if self.test else 0
        flags |= (1 << 0) if self.photo is not None else 0
        flags |= (1 << 2) if self.receipt_msg_id is not None else 0
        flags |= (1 << 4) if self.extended_media is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        if self.receipt_msg_id is not None:
            b.write(Int(self.receipt_msg_id))
        
        b.write(String(self.currency))
        
        b.write(Long(self.total_amount))
        
        b.write(String(self.start_param))
        
        if self.extended_media is not None:
            b.write(self.extended_media.write())
        
        return b.getvalue()
