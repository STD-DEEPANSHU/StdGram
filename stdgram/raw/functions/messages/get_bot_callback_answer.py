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


class GetBotCallbackAnswer(TLObject["raw.base.messages.BotCallbackAnswer"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``9342CA07``

    Parameters:
        peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        msg_id (``int`` ``32-bit``):
            N/A

        game (``bool``, *optional*):
            N/A

        data (``bytes``, *optional*):
            N/A

        password (:obj:`InputCheckPasswordSRP <stdgram.raw.base.InputCheckPasswordSRP>`, *optional*):
            N/A

    Returns:
        :obj:`messages.BotCallbackAnswer <stdgram.raw.base.messages.BotCallbackAnswer>`
    """

    __slots__: list[str] = ["peer", "msg_id", "game", "data", "password"]

    ID = 0x9342ca07
    QUALNAME = "functions.messages.GetBotCallbackAnswer"

    def __init__(self, *, peer: raw.base.InputPeer, msg_id: int, game: bool | None = None, data: bytes | None = None, password: raw.base.InputCheckPasswordSRP | None = None) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int
        self.game = game  # flags.1?true
        self.data = data  # flags.0?bytes
        self.password = password  # flags.2?InputCheckPasswordSRP

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GetBotCallbackAnswer:
        
        flags = Int.read(b)
        
        game = True if flags & (1 << 1) else False
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        data = Bytes.read(b) if flags & (1 << 0) else None
        password = TLObject.read(b) if flags & (1 << 2) else None
        
        return GetBotCallbackAnswer(peer=peer, msg_id=msg_id, game=game, data=data, password=password)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.game else 0
        flags |= (1 << 0) if self.data is not None else 0
        flags |= (1 << 2) if self.password is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        if self.data is not None:
            b.write(Bytes(self.data))
        
        if self.password is not None:
            b.write(self.password.write())
        
        return b.getvalue()
