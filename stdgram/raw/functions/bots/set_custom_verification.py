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


class SetCustomVerification(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``8B89DFBD``

    Parameters:
        peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        enabled (``bool``, *optional*):
            N/A

        bot (:obj:`InputUser <stdgram.raw.base.InputUser>`, *optional*):
            N/A

        custom_description (``str``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["peer", "enabled", "bot", "custom_description"]

    ID = 0x8b89dfbd
    QUALNAME = "functions.bots.SetCustomVerification"

    def __init__(self, *, peer: raw.base.InputPeer, enabled: bool | None = None, bot: raw.base.InputUser | None = None, custom_description: str | None = None) -> None:
        self.peer = peer  # InputPeer
        self.enabled = enabled  # flags.1?true
        self.bot = bot  # flags.0?InputUser
        self.custom_description = custom_description  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SetCustomVerification:
        
        flags = Int.read(b)
        
        enabled = True if flags & (1 << 1) else False
        bot = TLObject.read(b) if flags & (1 << 0) else None
        
        peer = TLObject.read(b)
        
        custom_description = String.read(b) if flags & (1 << 2) else None
        return SetCustomVerification(peer=peer, enabled=enabled, bot=bot, custom_description=custom_description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.enabled else 0
        flags |= (1 << 0) if self.bot is not None else 0
        flags |= (1 << 2) if self.custom_description is not None else 0
        b.write(Int(flags))
        
        if self.bot is not None:
            b.write(self.bot.write())
        
        b.write(self.peer.write())
        
        if self.custom_description is not None:
            b.write(String(self.custom_description))
        
        return b.getvalue()
