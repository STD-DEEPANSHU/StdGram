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


class HttpWait(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.HttpWait`.

    Details:
        - Layer: ``229``
        - ID: ``9299359F``

    Parameters:
        max_delay (``int`` ``32-bit``):
            N/A

        wait_after (``int`` ``32-bit``):
            N/A

        max_wait (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["max_delay", "wait_after", "max_wait"]

    ID = 0x9299359f
    QUALNAME = "types.HttpWait"

    def __init__(self, *, max_delay: int, wait_after: int, max_wait: int) -> None:
        self.max_delay = max_delay  # int
        self.wait_after = wait_after  # int
        self.max_wait = max_wait  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> HttpWait:
        # No flags
        
        max_delay = Int.read(b)
        
        wait_after = Int.read(b)
        
        max_wait = Int.read(b)
        
        return HttpWait(max_delay=max_delay, wait_after=wait_after, max_wait=max_wait)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.max_delay))
        
        b.write(Int(self.wait_after))
        
        b.write(Int(self.max_wait))
        
        return b.getvalue()
