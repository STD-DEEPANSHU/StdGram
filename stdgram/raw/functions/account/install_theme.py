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


class InstallTheme(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``C727BB3B``

    Parameters:
        dark (``bool``, *optional*):
            N/A

        theme (:obj:`InputTheme <stdgram.raw.base.InputTheme>`, *optional*):
            N/A

        format (``str``, *optional*):
            N/A

        base_theme (:obj:`BaseTheme <stdgram.raw.base.BaseTheme>`, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["dark", "theme", "format", "base_theme"]

    ID = 0xc727bb3b
    QUALNAME = "functions.account.InstallTheme"

    def __init__(self, *, dark: bool | None = None, theme: raw.base.InputTheme | None = None, format: str | None = None, base_theme: raw.base.BaseTheme | None = None) -> None:
        self.dark = dark  # flags.0?true
        self.theme = theme  # flags.1?InputTheme
        self.format = format  # flags.2?string
        self.base_theme = base_theme  # flags.3?BaseTheme

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InstallTheme:
        
        flags = Int.read(b)
        
        dark = True if flags & (1 << 0) else False
        theme = TLObject.read(b) if flags & (1 << 1) else None
        
        format = String.read(b) if flags & (1 << 2) else None
        base_theme = TLObject.read(b) if flags & (1 << 3) else None
        
        return InstallTheme(dark=dark, theme=theme, format=format, base_theme=base_theme)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.dark else 0
        flags |= (1 << 1) if self.theme is not None else 0
        flags |= (1 << 2) if self.format is not None else 0
        flags |= (1 << 3) if self.base_theme is not None else 0
        b.write(Int(flags))
        
        if self.theme is not None:
            b.write(self.theme.write())
        
        if self.format is not None:
            b.write(String(self.format))
        
        if self.base_theme is not None:
            b.write(self.base_theme.write())
        
        return b.getvalue()
