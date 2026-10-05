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


class TodoList(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.TodoList`.

    Details:
        - Layer: ``229``
        - ID: ``49B92A26``

    Parameters:
        title (:obj:`TextWithEntities <stdgram.raw.base.TextWithEntities>`):
            N/A

        list (List of :obj:`TodoItem <stdgram.raw.base.TodoItem>`):
            N/A

        others_can_append (``bool``, *optional*):
            N/A

        others_can_complete (``bool``, *optional*):
            N/A

    """

    __slots__: list[str] = ["title", "list", "others_can_append", "others_can_complete"]

    ID = 0x49b92a26
    QUALNAME = "types.TodoList"

    def __init__(self, *, title: raw.base.TextWithEntities, list: list[raw.base.TodoItem], others_can_append: bool | None = None, others_can_complete: bool | None = None) -> None:
        self.title = title  # TextWithEntities
        self.list = list  # Vector<TodoItem>
        self.others_can_append = others_can_append  # flags.0?true
        self.others_can_complete = others_can_complete  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> TodoList:
        
        flags = Int.read(b)
        
        others_can_append = True if flags & (1 << 0) else False
        others_can_complete = True if flags & (1 << 1) else False
        title = TLObject.read(b)
        
        list = TLObject.read(b)
        
        return TodoList(title=title, list=list, others_can_append=others_can_append, others_can_complete=others_can_complete)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.others_can_append else 0
        flags |= (1 << 1) if self.others_can_complete else 0
        b.write(Int(flags))
        
        b.write(self.title.write())
        
        b.write(Vector(self.list))
        
        return b.getvalue()
