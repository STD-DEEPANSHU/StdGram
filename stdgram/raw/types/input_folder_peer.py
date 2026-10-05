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


class InputFolderPeer(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputFolderPeer`.

    Details:
        - Layer: ``229``
        - ID: ``FBD2C296``

    Parameters:
        peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        folder_id (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["peer", "folder_id"]

    ID = 0xfbd2c296
    QUALNAME = "types.InputFolderPeer"

    def __init__(self, *, peer: raw.base.InputPeer, folder_id: int) -> None:
        self.peer = peer  # InputPeer
        self.folder_id = folder_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputFolderPeer:
        # No flags
        
        peer = TLObject.read(b)
        
        folder_id = Int.read(b)
        
        return InputFolderPeer(peer=peer, folder_id=folder_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.folder_id))
        
        return b.getvalue()
