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


class ReorderPinnedDialogs(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``3B1ADF37``

    Parameters:
        folder_id (``int`` ``32-bit``):
            N/A

        order (List of :obj:`InputDialogPeer <stdgram.raw.base.InputDialogPeer>`):
            N/A

        force (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["folder_id", "order", "force"]

    ID = 0x3b1adf37
    QUALNAME = "functions.messages.ReorderPinnedDialogs"

    def __init__(self, *, folder_id: int, order: list[raw.base.InputDialogPeer], force: bool | None = None) -> None:
        self.folder_id = folder_id  # int
        self.order = order  # Vector<InputDialogPeer>
        self.force = force  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> ReorderPinnedDialogs:
        
        flags = Int.read(b)
        
        force = True if flags & (1 << 0) else False
        folder_id = Int.read(b)
        
        order = TLObject.read(b)
        
        return ReorderPinnedDialogs(folder_id=folder_id, order=order, force=force)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.force else 0
        b.write(Int(flags))
        
        b.write(Int(self.folder_id))
        
        b.write(Vector(self.order))
        
        return b.getvalue()
