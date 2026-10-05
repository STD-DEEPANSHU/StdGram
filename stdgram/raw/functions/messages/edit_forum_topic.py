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


class EditForumTopic(TLObject["raw.base.Updates"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``CECC1134``

    Parameters:
        peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        topic_id (``int`` ``32-bit``):
            N/A

        title (``str``, *optional*):
            N/A

        icon_emoji_id (``int`` ``64-bit``, *optional*):
            N/A

        closed (``bool``, *optional*):
            N/A

        hidden (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <stdgram.raw.base.Updates>`
    """

    __slots__: list[str] = ["peer", "topic_id", "title", "icon_emoji_id", "closed", "hidden"]

    ID = 0xcecc1134
    QUALNAME = "functions.messages.EditForumTopic"

    def __init__(self, *, peer: raw.base.InputPeer, topic_id: int, title: str | None = None, icon_emoji_id: int | None = None, closed: bool | None = None, hidden: bool | None = None) -> None:
        self.peer = peer  # InputPeer
        self.topic_id = topic_id  # int
        self.title = title  # flags.0?string
        self.icon_emoji_id = icon_emoji_id  # flags.1?long
        self.closed = closed  # flags.2?Bool
        self.hidden = hidden  # flags.3?Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> EditForumTopic:
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        topic_id = Int.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        icon_emoji_id = Long.read(b) if flags & (1 << 1) else None
        closed = Bool.read(b) if flags & (1 << 2) else None
        hidden = Bool.read(b) if flags & (1 << 3) else None
        return EditForumTopic(peer=peer, topic_id=topic_id, title=title, icon_emoji_id=icon_emoji_id, closed=closed, hidden=hidden)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.title is not None else 0
        flags |= (1 << 1) if self.icon_emoji_id is not None else 0
        flags |= (1 << 2) if self.closed is not None else 0
        flags |= (1 << 3) if self.hidden is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.topic_id))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.icon_emoji_id is not None:
            b.write(Long(self.icon_emoji_id))
        
        if self.closed is not None:
            b.write(Bool(self.closed))
        
        if self.hidden is not None:
            b.write(Bool(self.hidden))
        
        return b.getvalue()
