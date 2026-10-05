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


class InputStickerSetShortName(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputStickerSet`.

    Details:
        - Layer: ``229``
        - ID: ``861CC8A0``

    Parameters:
        short_name (``str``):
            N/A

    """

    __slots__: list[str] = ["short_name"]

    ID = 0x861cc8a0
    QUALNAME = "types.InputStickerSetShortName"

    def __init__(self, *, short_name: str) -> None:
        self.short_name = short_name  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputStickerSetShortName:
        # No flags
        
        short_name = String.read(b)
        
        return InputStickerSetShortName(short_name=short_name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.short_name))
        
        return b.getvalue()
