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


class ReorderPinnedSavedDialogs(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``8B716587``

    Parameters:
        order (List of :obj:`InputDialogPeer <stdgram.raw.base.InputDialogPeer>`):
            N/A

        force (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["order", "force"]

    ID = 0x8b716587
    QUALNAME = "functions.messages.ReorderPinnedSavedDialogs"

    def __init__(self, *, order: list[raw.base.InputDialogPeer], force: bool | None = None) -> None:
        self.order = order  # Vector<InputDialogPeer>
        self.force = force  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> ReorderPinnedSavedDialogs:
        
        flags = Int.read(b)
        
        force = True if flags & (1 << 0) else False
        order = TLObject.read(b)
        
        return ReorderPinnedSavedDialogs(order=order, force=force)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.force else 0
        b.write(Int(flags))
        
        b.write(Vector(self.order))
        
        return b.getvalue()
