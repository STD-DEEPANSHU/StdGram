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


class StartBot(TLObject["raw.base.Updates"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``E6DF7378``

    Parameters:
        bot (:obj:`InputUser <stdgram.raw.base.InputUser>`):
            N/A

        peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        random_id (``int`` ``64-bit``):
            N/A

        start_param (``str``):
            N/A

    Returns:
        :obj:`Updates <stdgram.raw.base.Updates>`
    """

    __slots__: list[str] = ["bot", "peer", "random_id", "start_param"]

    ID = 0xe6df7378
    QUALNAME = "functions.messages.StartBot"

    def __init__(self, *, bot: raw.base.InputUser, peer: raw.base.InputPeer, random_id: int, start_param: str) -> None:
        self.bot = bot  # InputUser
        self.peer = peer  # InputPeer
        self.random_id = random_id  # long
        self.start_param = start_param  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> StartBot:
        # No flags
        
        bot = TLObject.read(b)
        
        peer = TLObject.read(b)
        
        random_id = Long.read(b)
        
        start_param = String.read(b)
        
        return StartBot(bot=bot, peer=peer, random_id=random_id, start_param=start_param)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot.write())
        
        b.write(self.peer.write())
        
        b.write(Long(self.random_id))
        
        b.write(String(self.start_param))
        
        return b.getvalue()
