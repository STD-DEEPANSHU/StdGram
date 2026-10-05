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


class GetTopPeers(TLObject["raw.base.contacts.TopPeers"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``973478B6``

    Parameters:
        offset (``int`` ``32-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        hash (``int`` ``64-bit``):
            N/A

        correspondents (``bool``, *optional*):
            N/A

        bots_pm (``bool``, *optional*):
            N/A

        bots_inline (``bool``, *optional*):
            N/A

        phone_calls (``bool``, *optional*):
            N/A

        forward_users (``bool``, *optional*):
            N/A

        forward_chats (``bool``, *optional*):
            N/A

        groups (``bool``, *optional*):
            N/A

        channels (``bool``, *optional*):
            N/A

        bots_app (``bool``, *optional*):
            N/A

        bots_guestchat (``bool``, *optional*):
            N/A

    Returns:
        :obj:`contacts.TopPeers <stdgram.raw.base.contacts.TopPeers>`
    """

    __slots__: list[str] = ["offset", "limit", "hash", "correspondents", "bots_pm", "bots_inline", "phone_calls", "forward_users", "forward_chats", "groups", "channels", "bots_app", "bots_guestchat"]

    ID = 0x973478b6
    QUALNAME = "functions.contacts.GetTopPeers"

    def __init__(self, *, offset: int, limit: int, hash: int, correspondents: bool | None = None, bots_pm: bool | None = None, bots_inline: bool | None = None, phone_calls: bool | None = None, forward_users: bool | None = None, forward_chats: bool | None = None, groups: bool | None = None, channels: bool | None = None, bots_app: bool | None = None, bots_guestchat: bool | None = None) -> None:
        self.offset = offset  # int
        self.limit = limit  # int
        self.hash = hash  # long
        self.correspondents = correspondents  # flags.0?true
        self.bots_pm = bots_pm  # flags.1?true
        self.bots_inline = bots_inline  # flags.2?true
        self.phone_calls = phone_calls  # flags.3?true
        self.forward_users = forward_users  # flags.4?true
        self.forward_chats = forward_chats  # flags.5?true
        self.groups = groups  # flags.10?true
        self.channels = channels  # flags.15?true
        self.bots_app = bots_app  # flags.16?true
        self.bots_guestchat = bots_guestchat  # flags.17?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GetTopPeers:
        
        flags = Int.read(b)
        
        correspondents = True if flags & (1 << 0) else False
        bots_pm = True if flags & (1 << 1) else False
        bots_inline = True if flags & (1 << 2) else False
        phone_calls = True if flags & (1 << 3) else False
        forward_users = True if flags & (1 << 4) else False
        forward_chats = True if flags & (1 << 5) else False
        groups = True if flags & (1 << 10) else False
        channels = True if flags & (1 << 15) else False
        bots_app = True if flags & (1 << 16) else False
        bots_guestchat = True if flags & (1 << 17) else False
        offset = Int.read(b)
        
        limit = Int.read(b)
        
        hash = Long.read(b)
        
        return GetTopPeers(offset=offset, limit=limit, hash=hash, correspondents=correspondents, bots_pm=bots_pm, bots_inline=bots_inline, phone_calls=phone_calls, forward_users=forward_users, forward_chats=forward_chats, groups=groups, channels=channels, bots_app=bots_app, bots_guestchat=bots_guestchat)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.correspondents else 0
        flags |= (1 << 1) if self.bots_pm else 0
        flags |= (1 << 2) if self.bots_inline else 0
        flags |= (1 << 3) if self.phone_calls else 0
        flags |= (1 << 4) if self.forward_users else 0
        flags |= (1 << 5) if self.forward_chats else 0
        flags |= (1 << 10) if self.groups else 0
        flags |= (1 << 15) if self.channels else 0
        flags |= (1 << 16) if self.bots_app else 0
        flags |= (1 << 17) if self.bots_guestchat else 0
        b.write(Int(flags))
        
        b.write(Int(self.offset))
        
        b.write(Int(self.limit))
        
        b.write(Long(self.hash))
        
        return b.getvalue()
