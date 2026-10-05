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


class ChannelDifferenceTooLong(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.updates.ChannelDifference`.

    Details:
        - Layer: ``229``
        - ID: ``A4BCC6FE``

    Parameters:
        dialog (:obj:`Dialog <stdgram.raw.base.Dialog>`):
            N/A

        messages (List of :obj:`Message <stdgram.raw.base.Message>`):
            N/A

        chats (List of :obj:`Chat <stdgram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <stdgram.raw.base.User>`):
            N/A

        final (``bool``, *optional*):
            N/A

        timeout (``int`` ``32-bit``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            updates.GetChannelDifference
    """

    __slots__: list[str] = ["dialog", "messages", "chats", "users", "final", "timeout"]

    ID = 0xa4bcc6fe
    QUALNAME = "types.updates.ChannelDifferenceTooLong"

    def __init__(self, *, dialog: raw.base.Dialog, messages: list[raw.base.Message], chats: list[raw.base.Chat], users: list[raw.base.User], final: bool | None = None, timeout: int | None = None) -> None:
        self.dialog = dialog  # Dialog
        self.messages = messages  # Vector<Message>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.final = final  # flags.0?true
        self.timeout = timeout  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> ChannelDifferenceTooLong:
        
        flags = Int.read(b)
        
        final = True if flags & (1 << 0) else False
        timeout = Int.read(b) if flags & (1 << 1) else None
        dialog = TLObject.read(b)
        
        messages = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return ChannelDifferenceTooLong(dialog=dialog, messages=messages, chats=chats, users=users, final=final, timeout=timeout)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.final else 0
        flags |= (1 << 1) if self.timeout is not None else 0
        b.write(Int(flags))
        
        if self.timeout is not None:
            b.write(Int(self.timeout))
        
        b.write(self.dialog.write())
        
        b.write(Vector(self.messages))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
