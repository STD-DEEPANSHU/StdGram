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


class RichButtonStyle(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.RichButtonStyle`.

    Details:
        - Layer: ``229``
        - ID: ``3C610BD``

    Parameters:
        bg_primary (``bool``, *optional*):
            N/A

        bg_danger (``bool``, *optional*):
            N/A

        bg_success (``bool``, *optional*):
            N/A

        link (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["bg_primary", "bg_danger", "bg_success", "link"]

    ID = 0x3c610bd
    QUALNAME = "types.RichButtonStyle"

    def __init__(self, *, bg_primary: bool | None = None, bg_danger: bool | None = None, bg_success: bool | None = None, link: bool | None = None) -> None:
        self.bg_primary = bg_primary  # flags.0?true
        self.bg_danger = bg_danger  # flags.1?true
        self.bg_success = bg_success  # flags.2?true
        self.link = link  # flags.3?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> RichButtonStyle:
        
        flags = Int.read(b)
        
        bg_primary = True if flags & (1 << 0) else False
        bg_danger = True if flags & (1 << 1) else False
        bg_success = True if flags & (1 << 2) else False
        link = True if flags & (1 << 3) else False
        return RichButtonStyle(bg_primary=bg_primary, bg_danger=bg_danger, bg_success=bg_success, link=link)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.bg_primary else 0
        flags |= (1 << 1) if self.bg_danger else 0
        flags |= (1 << 2) if self.bg_success else 0
        flags |= (1 << 3) if self.link else 0
        b.write(Int(flags))
        
        return b.getvalue()
