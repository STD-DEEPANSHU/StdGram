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


class StarGiftAttributeModel(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.StarGiftAttribute`.

    Details:
        - Layer: ``229``
        - ID: ``565251E2``

    Parameters:
        name (``str``):
            N/A

        document (:obj:`Document <stdgram.raw.base.Document>`):
            N/A

        rarity (:obj:`StarGiftAttributeRarity <stdgram.raw.base.StarGiftAttributeRarity>`):
            N/A

        crafted (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["name", "document", "rarity", "crafted"]

    ID = 0x565251e2
    QUALNAME = "types.StarGiftAttributeModel"

    def __init__(self, *, name: str, document: raw.base.Document, rarity: raw.base.StarGiftAttributeRarity, crafted: bool | None = None) -> None:
        self.name = name  # string
        self.document = document  # Document
        self.rarity = rarity  # StarGiftAttributeRarity
        self.crafted = crafted  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> StarGiftAttributeModel:
        
        flags = Int.read(b)
        
        crafted = True if flags & (1 << 0) else False
        name = String.read(b)
        
        document = TLObject.read(b)
        
        rarity = TLObject.read(b)
        
        return StarGiftAttributeModel(name=name, document=document, rarity=rarity, crafted=crafted)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.crafted else 0
        b.write(Int(flags))
        
        b.write(String(self.name))
        
        b.write(self.document.write())
        
        b.write(self.rarity.write())
        
        return b.getvalue()
