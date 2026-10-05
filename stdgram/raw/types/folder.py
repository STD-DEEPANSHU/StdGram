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


class Folder(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.Folder`.

    Details:
        - Layer: ``229``
        - ID: ``FF544E65``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        title (``str``):
            N/A

        autofill_new_broadcasts (``bool``, *optional*):
            N/A

        autofill_public_groups (``bool``, *optional*):
            N/A

        autofill_new_correspondents (``bool``, *optional*):
            N/A

        photo (:obj:`ChatPhoto <stdgram.raw.base.ChatPhoto>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["id", "title", "autofill_new_broadcasts", "autofill_public_groups", "autofill_new_correspondents", "photo"]

    ID = 0xff544e65
    QUALNAME = "types.Folder"

    def __init__(self, *, id: int, title: str, autofill_new_broadcasts: bool | None = None, autofill_public_groups: bool | None = None, autofill_new_correspondents: bool | None = None, photo: raw.base.ChatPhoto | None = None) -> None:
        self.id = id  # int
        self.title = title  # string
        self.autofill_new_broadcasts = autofill_new_broadcasts  # flags.0?true
        self.autofill_public_groups = autofill_public_groups  # flags.1?true
        self.autofill_new_correspondents = autofill_new_correspondents  # flags.2?true
        self.photo = photo  # flags.3?ChatPhoto

    @staticmethod
    def read(b: BytesIO, *args: Any) -> Folder:
        
        flags = Int.read(b)
        
        autofill_new_broadcasts = True if flags & (1 << 0) else False
        autofill_public_groups = True if flags & (1 << 1) else False
        autofill_new_correspondents = True if flags & (1 << 2) else False
        id = Int.read(b)
        
        title = String.read(b)
        
        photo = TLObject.read(b) if flags & (1 << 3) else None
        
        return Folder(id=id, title=title, autofill_new_broadcasts=autofill_new_broadcasts, autofill_public_groups=autofill_public_groups, autofill_new_correspondents=autofill_new_correspondents, photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.autofill_new_broadcasts else 0
        flags |= (1 << 1) if self.autofill_public_groups else 0
        flags |= (1 << 2) if self.autofill_new_correspondents else 0
        flags |= (1 << 3) if self.photo is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(String(self.title))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        return b.getvalue()
