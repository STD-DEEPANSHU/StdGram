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


class GetBroadcastStats(TLObject["raw.base.stats.BroadcastStats"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``AB42441A``

    Parameters:
        channel (:obj:`InputChannel <stdgram.raw.base.InputChannel>`):
            N/A

        dark (``bool``, *optional*):
            N/A

    Returns:
        :obj:`stats.BroadcastStats <stdgram.raw.base.stats.BroadcastStats>`
    """

    __slots__: list[str] = ["channel", "dark"]

    ID = 0xab42441a
    QUALNAME = "functions.stats.GetBroadcastStats"

    def __init__(self, *, channel: raw.base.InputChannel, dark: bool | None = None) -> None:
        self.channel = channel  # InputChannel
        self.dark = dark  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GetBroadcastStats:
        
        flags = Int.read(b)
        
        dark = True if flags & (1 << 0) else False
        channel = TLObject.read(b)
        
        return GetBroadcastStats(channel=channel, dark=dark)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.dark else 0
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        return b.getvalue()
