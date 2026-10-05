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


class SaveAutoSaveSettings(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``D69B8361``

    Parameters:
        settings (:obj:`AutoSaveSettings <stdgram.raw.base.AutoSaveSettings>`):
            N/A

        users (``bool``, *optional*):
            N/A

        chats (``bool``, *optional*):
            N/A

        broadcasts (``bool``, *optional*):
            N/A

        peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["settings", "users", "chats", "broadcasts", "peer"]

    ID = 0xd69b8361
    QUALNAME = "functions.account.SaveAutoSaveSettings"

    def __init__(self, *, settings: raw.base.AutoSaveSettings, users: bool | None = None, chats: bool | None = None, broadcasts: bool | None = None, peer: raw.base.InputPeer | None = None) -> None:
        self.settings = settings  # AutoSaveSettings
        self.users = users  # flags.0?true
        self.chats = chats  # flags.1?true
        self.broadcasts = broadcasts  # flags.2?true
        self.peer = peer  # flags.3?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SaveAutoSaveSettings:
        
        flags = Int.read(b)
        
        users = True if flags & (1 << 0) else False
        chats = True if flags & (1 << 1) else False
        broadcasts = True if flags & (1 << 2) else False
        peer = TLObject.read(b) if flags & (1 << 3) else None
        
        settings = TLObject.read(b)
        
        return SaveAutoSaveSettings(settings=settings, users=users, chats=chats, broadcasts=broadcasts, peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.users else 0
        flags |= (1 << 1) if self.chats else 0
        flags |= (1 << 2) if self.broadcasts else 0
        flags |= (1 << 3) if self.peer is not None else 0
        b.write(Int(flags))
        
        if self.peer is not None:
            b.write(self.peer.write())
        
        b.write(self.settings.write())
        
        return b.getvalue()
