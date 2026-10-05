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


class Create(TLObject["raw.base.Updates"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``A63859EC``

    Parameters:
        title (``str``):
            N/A

        peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        hidden (``bool``, *optional*):
            N/A

        about (``str``, *optional*):
            N/A

    Returns:
        :obj:`Updates <stdgram.raw.base.Updates>`
    """

    __slots__: list[str] = ["title", "peer", "hidden", "about"]

    ID = 0xa63859ec
    QUALNAME = "functions.communities.Create"

    def __init__(self, *, title: str, peer: raw.base.InputPeer, hidden: bool | None = None, about: str | None = None) -> None:
        self.title = title  # string
        self.peer = peer  # InputPeer
        self.hidden = hidden  # flags.1?true
        self.about = about  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> Create:
        
        flags = Int.read(b)
        
        hidden = True if flags & (1 << 1) else False
        title = String.read(b)
        
        about = String.read(b) if flags & (1 << 0) else None
        peer = TLObject.read(b)
        
        return Create(title=title, peer=peer, hidden=hidden, about=about)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.hidden else 0
        flags |= (1 << 0) if self.about is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        if self.about is not None:
            b.write(String(self.about))
        
        b.write(self.peer.write())
        
        return b.getvalue()
