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


class InputRichMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputRichMessage`.

    Details:
        - Layer: ``229``
        - ID: ``E4C449FC``

    Parameters:
        blocks (List of :obj:`PageBlock <stdgram.raw.base.PageBlock>`):
            N/A

        rtl (``bool``, *optional*):
            N/A

        noautolink (``bool``, *optional*):
            N/A

        photos (List of :obj:`InputPhoto <stdgram.raw.base.InputPhoto>`, *optional*):
            N/A

        documents (List of :obj:`InputDocument <stdgram.raw.base.InputDocument>`, *optional*):
            N/A

        users (List of :obj:`InputUser <stdgram.raw.base.InputUser>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["blocks", "rtl", "noautolink", "photos", "documents", "users"]

    ID = 0xe4c449fc
    QUALNAME = "types.InputRichMessage"

    def __init__(self, *, blocks: list[raw.base.PageBlock], rtl: bool | None = None, noautolink: bool | None = None, photos: list[raw.base.InputPhoto] | None = None, documents: list[raw.base.InputDocument] | None = None, users: list[raw.base.InputUser] | None = None) -> None:
        self.blocks = blocks  # Vector<PageBlock>
        self.rtl = rtl  # flags.0?true
        self.noautolink = noautolink  # flags.1?true
        self.photos = photos  # flags.2?Vector<InputPhoto>
        self.documents = documents  # flags.3?Vector<InputDocument>
        self.users = users  # flags.4?Vector<InputUser>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputRichMessage:
        
        flags = Int.read(b)
        
        rtl = True if flags & (1 << 0) else False
        noautolink = True if flags & (1 << 1) else False
        blocks = TLObject.read(b)
        
        photos = TLObject.read(b) if flags & (1 << 2) else []
        
        documents = TLObject.read(b) if flags & (1 << 3) else []
        
        users = TLObject.read(b) if flags & (1 << 4) else []
        
        return InputRichMessage(blocks=blocks, rtl=rtl, noautolink=noautolink, photos=photos, documents=documents, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.rtl else 0
        flags |= (1 << 1) if self.noautolink else 0
        flags |= (1 << 2) if self.photos else 0
        flags |= (1 << 3) if self.documents else 0
        flags |= (1 << 4) if self.users else 0
        b.write(Int(flags))
        
        b.write(Vector(self.blocks))
        
        if self.photos is not None:
            b.write(Vector(self.photos))
        
        if self.documents is not None:
            b.write(Vector(self.documents))
        
        if self.users is not None:
            b.write(Vector(self.users))
        
        return b.getvalue()
