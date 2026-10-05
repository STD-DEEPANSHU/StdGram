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


class InputSavedStarGiftChat(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputSavedStarGift`.

    Details:
        - Layer: ``229``
        - ID: ``F101AA7F``

    Parameters:
        peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        saved_id (``int`` ``64-bit``):
            N/A

    """

    __slots__: list[str] = ["peer", "saved_id"]

    ID = 0xf101aa7f
    QUALNAME = "types.InputSavedStarGiftChat"

    def __init__(self, *, peer: raw.base.InputPeer, saved_id: int) -> None:
        self.peer = peer  # InputPeer
        self.saved_id = saved_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputSavedStarGiftChat:
        # No flags
        
        peer = TLObject.read(b)
        
        saved_id = Long.read(b)
        
        return InputSavedStarGiftChat(peer=peer, saved_id=saved_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Long(self.saved_id))
        
        return b.getvalue()
