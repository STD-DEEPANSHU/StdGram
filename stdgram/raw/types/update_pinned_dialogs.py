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


class UpdatePinnedDialogs(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.Update`.

    Details:
        - Layer: ``229``
        - ID: ``FA0F3CA2``

    Parameters:
        folder_id (``int`` ``32-bit``, *optional*):
            N/A

        order (List of :obj:`DialogPeer <stdgram.raw.base.DialogPeer>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["folder_id", "order"]

    ID = 0xfa0f3ca2
    QUALNAME = "types.UpdatePinnedDialogs"

    def __init__(self, *, folder_id: int | None = None, order: list[raw.base.DialogPeer] | None = None) -> None:
        self.folder_id = folder_id  # flags.1?int
        self.order = order  # flags.0?Vector<DialogPeer>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdatePinnedDialogs:
        
        flags = Int.read(b)
        
        folder_id = Int.read(b) if flags & (1 << 1) else None
        order = TLObject.read(b) if flags & (1 << 0) else []
        
        return UpdatePinnedDialogs(folder_id=folder_id, order=order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.folder_id is not None else 0
        flags |= (1 << 0) if self.order else 0
        b.write(Int(flags))
        
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        
        if self.order is not None:
            b.write(Vector(self.order))
        
        return b.getvalue()
