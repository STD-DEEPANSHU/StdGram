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


class UpdateGroupCall(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.Update`.

    Details:
        - Layer: ``229``
        - ID: ``9D2216E0``

    Parameters:
        call (:obj:`GroupCall <stdgram.raw.base.GroupCall>`):
            N/A

        live_story (``bool``, *optional*):
            N/A

        peer (:obj:`Peer <stdgram.raw.base.Peer>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["call", "live_story", "peer"]

    ID = 0x9d2216e0
    QUALNAME = "types.UpdateGroupCall"

    def __init__(self, *, call: raw.base.GroupCall, live_story: bool | None = None, peer: raw.base.Peer | None = None) -> None:
        self.call = call  # GroupCall
        self.live_story = live_story  # flags.2?true
        self.peer = peer  # flags.1?Peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateGroupCall:
        
        flags = Int.read(b)
        
        live_story = True if flags & (1 << 2) else False
        peer = TLObject.read(b) if flags & (1 << 1) else None
        
        call = TLObject.read(b)
        
        return UpdateGroupCall(call=call, live_story=live_story, peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.live_story else 0
        flags |= (1 << 1) if self.peer is not None else 0
        b.write(Int(flags))
        
        if self.peer is not None:
            b.write(self.peer.write())
        
        b.write(self.call.write())
        
        return b.getvalue()
