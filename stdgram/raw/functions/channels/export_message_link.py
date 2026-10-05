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


class ExportMessageLink(TLObject["raw.base.ExportedMessageLink"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``E63FADEB``

    Parameters:
        channel (:obj:`InputChannel <stdgram.raw.base.InputChannel>`):
            N/A

        id (``int`` ``32-bit``):
            N/A

        grouped (``bool``, *optional*):
            N/A

        thread (``bool``, *optional*):
            N/A

    Returns:
        :obj:`ExportedMessageLink <stdgram.raw.base.ExportedMessageLink>`
    """

    __slots__: list[str] = ["channel", "id", "grouped", "thread"]

    ID = 0xe63fadeb
    QUALNAME = "functions.channels.ExportMessageLink"

    def __init__(self, *, channel: raw.base.InputChannel, id: int, grouped: bool | None = None, thread: bool | None = None) -> None:
        self.channel = channel  # InputChannel
        self.id = id  # int
        self.grouped = grouped  # flags.0?true
        self.thread = thread  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> ExportMessageLink:
        
        flags = Int.read(b)
        
        grouped = True if flags & (1 << 0) else False
        thread = True if flags & (1 << 1) else False
        channel = TLObject.read(b)
        
        id = Int.read(b)
        
        return ExportMessageLink(channel=channel, id=id, grouped=grouped, thread=thread)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.grouped else 0
        flags |= (1 << 1) if self.thread else 0
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        b.write(Int(self.id))
        
        return b.getvalue()
