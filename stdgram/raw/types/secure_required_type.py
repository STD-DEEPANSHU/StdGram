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


class SecureRequiredType(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.SecureRequiredType`.

    Details:
        - Layer: ``229``
        - ID: ``829D99DA``

    Parameters:
        type (:obj:`SecureValueType <stdgram.raw.base.SecureValueType>`):
            N/A

        native_names (``bool``, *optional*):
            N/A

        selfie_required (``bool``, *optional*):
            N/A

        translation_required (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["type", "native_names", "selfie_required", "translation_required"]

    ID = 0x829d99da
    QUALNAME = "types.SecureRequiredType"

    def __init__(self, *, type: raw.base.SecureValueType, native_names: bool | None = None, selfie_required: bool | None = None, translation_required: bool | None = None) -> None:
        self.type = type  # SecureValueType
        self.native_names = native_names  # flags.0?true
        self.selfie_required = selfie_required  # flags.1?true
        self.translation_required = translation_required  # flags.2?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SecureRequiredType:
        
        flags = Int.read(b)
        
        native_names = True if flags & (1 << 0) else False
        selfie_required = True if flags & (1 << 1) else False
        translation_required = True if flags & (1 << 2) else False
        type = TLObject.read(b)
        
        return SecureRequiredType(type=type, native_names=native_names, selfie_required=selfie_required, translation_required=translation_required)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.native_names else 0
        flags |= (1 << 1) if self.selfie_required else 0
        flags |= (1 << 2) if self.translation_required else 0
        b.write(Int(flags))
        
        b.write(self.type.write())
        
        return b.getvalue()
