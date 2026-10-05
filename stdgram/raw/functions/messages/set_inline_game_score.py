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


class SetInlineGameScore(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``15AD9F64``

    Parameters:
        id (:obj:`InputBotInlineMessageID <stdgram.raw.base.InputBotInlineMessageID>`):
            N/A

        user_id (:obj:`InputUser <stdgram.raw.base.InputUser>`):
            N/A

        score (``int`` ``32-bit``):
            N/A

        edit_message (``bool``, *optional*):
            N/A

        force (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["id", "user_id", "score", "edit_message", "force"]

    ID = 0x15ad9f64
    QUALNAME = "functions.messages.SetInlineGameScore"

    def __init__(self, *, id: raw.base.InputBotInlineMessageID, user_id: raw.base.InputUser, score: int, edit_message: bool | None = None, force: bool | None = None) -> None:
        self.id = id  # InputBotInlineMessageID
        self.user_id = user_id  # InputUser
        self.score = score  # int
        self.edit_message = edit_message  # flags.0?true
        self.force = force  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SetInlineGameScore:
        
        flags = Int.read(b)
        
        edit_message = True if flags & (1 << 0) else False
        force = True if flags & (1 << 1) else False
        id = TLObject.read(b)
        
        user_id = TLObject.read(b)
        
        score = Int.read(b)
        
        return SetInlineGameScore(id=id, user_id=user_id, score=score, edit_message=edit_message, force=force)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.edit_message else 0
        flags |= (1 << 1) if self.force else 0
        b.write(Int(flags))
        
        b.write(self.id.write())
        
        b.write(self.user_id.write())
        
        b.write(Int(self.score))
        
        return b.getvalue()
