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


class BotCommand(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.BotCommand`.

    Details:
        - Layer: ``229``
        - ID: ``9852D6D2``

    Parameters:
        command (``str``):
            N/A

        description (``str``):
            N/A

        ephemeral (``bool``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetBotCommands
    """

    __slots__: list[str] = ["command", "description", "ephemeral"]

    ID = 0x9852d6d2
    QUALNAME = "types.BotCommand"

    def __init__(self, *, command: str, description: str, ephemeral: bool | None = None) -> None:
        self.command = command  # string
        self.description = description  # string
        self.ephemeral = ephemeral  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> BotCommand:
        
        flags = Int.read(b)
        
        ephemeral = True if flags & (1 << 0) else False
        command = String.read(b)
        
        description = String.read(b)
        
        return BotCommand(command=command, description=description, ephemeral=ephemeral)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.ephemeral else 0
        b.write(Int(flags))
        
        b.write(String(self.command))
        
        b.write(String(self.description))
        
        return b.getvalue()
