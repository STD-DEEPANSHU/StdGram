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


class SendMessageEmojiInteraction(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.SendMessageAction`.

    Details:
        - Layer: ``229``
        - ID: ``25972BCB``

    Parameters:
        emoticon (``str``):
            N/A

        msg_id (``int`` ``32-bit``):
            N/A

        interaction (:obj:`DataJSON <stdgram.raw.base.DataJSON>`):
            N/A

    """

    __slots__: list[str] = ["emoticon", "msg_id", "interaction"]

    ID = 0x25972bcb
    QUALNAME = "types.SendMessageEmojiInteraction"

    def __init__(self, *, emoticon: str, msg_id: int, interaction: raw.base.DataJSON) -> None:
        self.emoticon = emoticon  # string
        self.msg_id = msg_id  # int
        self.interaction = interaction  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SendMessageEmojiInteraction:
        # No flags
        
        emoticon = String.read(b)
        
        msg_id = Int.read(b)
        
        interaction = TLObject.read(b)
        
        return SendMessageEmojiInteraction(emoticon=emoticon, msg_id=msg_id, interaction=interaction)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.emoticon))
        
        b.write(Int(self.msg_id))
        
        b.write(self.interaction.write())
        
        return b.getvalue()
