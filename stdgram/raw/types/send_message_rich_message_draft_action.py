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


class SendMessageRichMessageDraftAction(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.SendMessageAction`.

    Details:
        - Layer: ``229``
        - ID: ``52564893``

    Parameters:
        random_id (``int`` ``64-bit``):
            N/A

        rich_message (:obj:`RichMessage <stdgram.raw.base.RichMessage>`):
            N/A

        can_stop (``bool``, *optional*):
            N/A

        keep_on_stop (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["random_id", "rich_message", "can_stop", "keep_on_stop"]

    ID = 0x52564893
    QUALNAME = "types.SendMessageRichMessageDraftAction"

    def __init__(self, *, random_id: int, rich_message: raw.base.RichMessage, can_stop: bool | None = None, keep_on_stop: bool | None = None) -> None:
        self.random_id = random_id  # long
        self.rich_message = rich_message  # RichMessage
        self.can_stop = can_stop  # flags.0?true
        self.keep_on_stop = keep_on_stop  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SendMessageRichMessageDraftAction:
        
        flags = Int.read(b)
        
        can_stop = True if flags & (1 << 0) else False
        keep_on_stop = True if flags & (1 << 1) else False
        random_id = Long.read(b)
        
        rich_message = TLObject.read(b)
        
        return SendMessageRichMessageDraftAction(random_id=random_id, rich_message=rich_message, can_stop=can_stop, keep_on_stop=keep_on_stop)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.can_stop else 0
        flags |= (1 << 1) if self.keep_on_stop else 0
        b.write(Int(flags))
        
        b.write(Long(self.random_id))
        
        b.write(self.rich_message.write())
        
        return b.getvalue()
