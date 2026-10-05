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


class DialogCommunity(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.Dialog`.

    Details:
        - Layer: ``229``
        - ID: ``F78A0973``

    Parameters:
        community_id (``int`` ``64-bit``):
            N/A

        notify_settings (:obj:`PeerNotifySettings <stdgram.raw.base.PeerNotifySettings>`):
            N/A

        pinned (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["community_id", "notify_settings", "pinned"]

    ID = 0xf78a0973
    QUALNAME = "types.DialogCommunity"

    def __init__(self, *, community_id: int, notify_settings: raw.base.PeerNotifySettings, pinned: bool | None = None) -> None:
        self.community_id = community_id  # long
        self.notify_settings = notify_settings  # PeerNotifySettings
        self.pinned = pinned  # flags.2?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> DialogCommunity:
        
        flags = Int.read(b)
        
        pinned = True if flags & (1 << 2) else False
        community_id = Long.read(b)
        
        notify_settings = TLObject.read(b)
        
        return DialogCommunity(community_id=community_id, notify_settings=notify_settings, pinned=pinned)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.pinned else 0
        b.write(Int(flags))
        
        b.write(Long(self.community_id))
        
        b.write(self.notify_settings.write())
        
        return b.getvalue()
