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


class InputMediaInvoice(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputMedia`.

    Details:
        - Layer: ``229``
        - ID: ``405FEF0D``

    Parameters:
        title (``str``):
            N/A

        description (``str``):
            N/A

        invoice (:obj:`Invoice <stdgram.raw.base.Invoice>`):
            N/A

        payload (``bytes``):
            N/A

        provider_data (:obj:`DataJSON <stdgram.raw.base.DataJSON>`):
            N/A

        photo (:obj:`InputWebDocument <stdgram.raw.base.InputWebDocument>`, *optional*):
            N/A

        provider (``str``, *optional*):
            N/A

        start_param (``str``, *optional*):
            N/A

        extended_media (:obj:`InputMedia <stdgram.raw.base.InputMedia>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["title", "description", "invoice", "payload", "provider_data", "photo", "provider", "start_param", "extended_media"]

    ID = 0x405fef0d
    QUALNAME = "types.InputMediaInvoice"

    def __init__(self, *, title: str, description: str, invoice: raw.base.Invoice, payload: bytes, provider_data: raw.base.DataJSON, photo: raw.base.InputWebDocument | None = None, provider: str | None = None, start_param: str | None = None, extended_media: raw.base.InputMedia | None = None) -> None:
        self.title = title  # string
        self.description = description  # string
        self.invoice = invoice  # Invoice
        self.payload = payload  # bytes
        self.provider_data = provider_data  # DataJSON
        self.photo = photo  # flags.0?InputWebDocument
        self.provider = provider  # flags.3?string
        self.start_param = start_param  # flags.1?string
        self.extended_media = extended_media  # flags.2?InputMedia

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputMediaInvoice:
        
        flags = Int.read(b)
        
        title = String.read(b)
        
        description = String.read(b)
        
        photo = TLObject.read(b) if flags & (1 << 0) else None
        
        invoice = TLObject.read(b)
        
        payload = Bytes.read(b)
        
        provider = String.read(b) if flags & (1 << 3) else None
        provider_data = TLObject.read(b)
        
        start_param = String.read(b) if flags & (1 << 1) else None
        extended_media = TLObject.read(b) if flags & (1 << 2) else None
        
        return InputMediaInvoice(title=title, description=description, invoice=invoice, payload=payload, provider_data=provider_data, photo=photo, provider=provider, start_param=start_param, extended_media=extended_media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.photo is not None else 0
        flags |= (1 << 3) if self.provider is not None else 0
        flags |= (1 << 1) if self.start_param is not None else 0
        flags |= (1 << 2) if self.extended_media is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        b.write(self.invoice.write())
        
        b.write(Bytes(self.payload))
        
        if self.provider is not None:
            b.write(String(self.provider))
        
        b.write(self.provider_data.write())
        
        if self.start_param is not None:
            b.write(String(self.start_param))
        
        if self.extended_media is not None:
            b.write(self.extended_media.write())
        
        return b.getvalue()
