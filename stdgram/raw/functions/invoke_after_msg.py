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
from stdgram.raw.core import TLObject, ReturnType

if TYPE_CHECKING:
    from stdgram import raw

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class InvokeAfterMsg(TLObject[ReturnType]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``CB9F372D``

    Parameters:
        msg_id (``int`` ``64-bit``):
            N/A

        query (Any function from :obj:`~stdgram.raw.functions`):
            N/A

    Returns:
        Any object from :obj:`~stdgram.raw.types`
    """

    __slots__: list[str] = ["msg_id", "query"]

    ID = 0xcb9f372d
    QUALNAME = "functions.InvokeAfterMsg"

    def __init__(self, *, msg_id: int, query: TLObject[ReturnType]) -> None:
        self.msg_id = msg_id  # long
        self.query = query  # !X

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InvokeAfterMsg:
        # No flags
        
        msg_id = Long.read(b)
        
        query = TLObject.read(b)
        
        return InvokeAfterMsg(msg_id=msg_id, query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.msg_id))
        
        b.write(self.query.write())
        
        return b.getvalue()
