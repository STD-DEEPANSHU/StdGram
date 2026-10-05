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


class InputInvoiceStarGiftResale(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputInvoice`.

    Details:
        - Layer: ``229``
        - ID: ``E9B0C658``

    Parameters:
        slug (``str``):
            N/A

        to_id (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        ton (``bool``, *optional*):
            N/A

        show_name (``bool``, *optional*):
            N/A

        message (:obj:`TextWithEntities <stdgram.raw.base.TextWithEntities>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["slug", "to_id", "ton", "show_name", "message"]

    ID = 0xe9b0c658
    QUALNAME = "types.InputInvoiceStarGiftResale"

    def __init__(self, *, slug: str, to_id: raw.base.InputPeer, ton: bool | None = None, show_name: bool | None = None, message: raw.base.TextWithEntities | None = None) -> None:
        self.slug = slug  # string
        self.to_id = to_id  # InputPeer
        self.ton = ton  # flags.0?true
        self.show_name = show_name  # flags.2?true
        self.message = message  # flags.1?TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputInvoiceStarGiftResale:
        
        flags = Int.read(b)
        
        ton = True if flags & (1 << 0) else False
        show_name = True if flags & (1 << 2) else False
        slug = String.read(b)
        
        to_id = TLObject.read(b)
        
        message = TLObject.read(b) if flags & (1 << 1) else None
        
        return InputInvoiceStarGiftResale(slug=slug, to_id=to_id, ton=ton, show_name=show_name, message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.ton else 0
        flags |= (1 << 2) if self.show_name else 0
        flags |= (1 << 1) if self.message is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.slug))
        
        b.write(self.to_id.write())
        
        if self.message is not None:
            b.write(self.message.write())
        
        return b.getvalue()
