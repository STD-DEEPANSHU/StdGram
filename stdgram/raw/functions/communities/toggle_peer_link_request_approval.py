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


class TogglePeerLinkRequestApproval(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``8C8219A8``

    Parameters:
        community (:obj:`InputChannel <stdgram.raw.base.InputChannel>`):
            N/A

        peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        reject (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["community", "peer", "reject"]

    ID = 0x8c8219a8
    QUALNAME = "functions.communities.TogglePeerLinkRequestApproval"

    def __init__(self, *, community: raw.base.InputChannel, peer: raw.base.InputPeer, reject: bool | None = None) -> None:
        self.community = community  # InputChannel
        self.peer = peer  # InputPeer
        self.reject = reject  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> TogglePeerLinkRequestApproval:
        
        flags = Int.read(b)
        
        reject = True if flags & (1 << 0) else False
        community = TLObject.read(b)
        
        peer = TLObject.read(b)
        
        return TogglePeerLinkRequestApproval(community=community, peer=peer, reject=reject)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.reject else 0
        b.write(Int(flags))
        
        b.write(self.community.write())
        
        b.write(self.peer.write())
        
        return b.getvalue()
