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


class TogglePeerLink(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``736DCFEA``

    Parameters:
        community (:obj:`InputChannel <stdgram.raw.base.InputChannel>`):
            N/A

        peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        visible (``bool``, *optional*):
            N/A

        hidden (``bool``, *optional*):
            N/A

        deleted (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["community", "peer", "visible", "hidden", "deleted"]

    ID = 0x736dcfea
    QUALNAME = "functions.communities.TogglePeerLink"

    def __init__(self, *, community: raw.base.InputChannel, peer: raw.base.InputPeer, visible: bool | None = None, hidden: bool | None = None, deleted: bool | None = None) -> None:
        self.community = community  # InputChannel
        self.peer = peer  # InputPeer
        self.visible = visible  # flags.0?true
        self.hidden = hidden  # flags.1?true
        self.deleted = deleted  # flags.2?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> TogglePeerLink:
        
        flags = Int.read(b)
        
        visible = True if flags & (1 << 0) else False
        hidden = True if flags & (1 << 1) else False
        deleted = True if flags & (1 << 2) else False
        community = TLObject.read(b)
        
        peer = TLObject.read(b)
        
        return TogglePeerLink(community=community, peer=peer, visible=visible, hidden=hidden, deleted=deleted)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.visible else 0
        flags |= (1 << 1) if self.hidden else 0
        flags |= (1 << 2) if self.deleted else 0
        b.write(Int(flags))
        
        b.write(self.community.write())
        
        b.write(self.peer.write())
        
        return b.getvalue()
