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


class InputWebFileAudioAlbumThumbLocation(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputWebFileLocation`.

    Details:
        - Layer: ``229``
        - ID: ``F46FE924``

    Parameters:
        small (``bool``, *optional*):
            N/A

        document (:obj:`InputDocument <stdgram.raw.base.InputDocument>`, *optional*):
            N/A

        title (``str``, *optional*):
            N/A

        performer (``str``, *optional*):
            N/A

    """

    __slots__: list[str] = ["small", "document", "title", "performer"]

    ID = 0xf46fe924
    QUALNAME = "types.InputWebFileAudioAlbumThumbLocation"

    def __init__(self, *, small: bool | None = None, document: raw.base.InputDocument | None = None, title: str | None = None, performer: str | None = None) -> None:
        self.small = small  # flags.2?true
        self.document = document  # flags.0?InputDocument
        self.title = title  # flags.1?string
        self.performer = performer  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputWebFileAudioAlbumThumbLocation:
        
        flags = Int.read(b)
        
        small = True if flags & (1 << 2) else False
        document = TLObject.read(b) if flags & (1 << 0) else None
        
        title = String.read(b) if flags & (1 << 1) else None
        performer = String.read(b) if flags & (1 << 1) else None
        return InputWebFileAudioAlbumThumbLocation(small=small, document=document, title=title, performer=performer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.small else 0
        flags |= (1 << 0) if self.document is not None else 0
        flags |= (1 << 1) if self.title is not None else 0
        flags |= (1 << 1) if self.performer is not None else 0
        b.write(Int(flags))
        
        if self.document is not None:
            b.write(self.document.write())
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.performer is not None:
            b.write(String(self.performer))
        
        return b.getvalue()
