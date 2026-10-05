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


class InputMessageReadMetric(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputMessageReadMetric`.

    Details:
        - Layer: ``229``
        - ID: ``402B4495``

    Parameters:
        msg_id (``int`` ``32-bit``):
            N/A

        view_id (``int`` ``64-bit``):
            N/A

        time_in_view_ms (``int`` ``32-bit``):
            N/A

        active_time_in_view_ms (``int`` ``32-bit``):
            N/A

        height_to_viewport_ratio_permille (``int`` ``32-bit``):
            N/A

        seen_range_ratio_permille (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["msg_id", "view_id", "time_in_view_ms", "active_time_in_view_ms", "height_to_viewport_ratio_permille", "seen_range_ratio_permille"]

    ID = 0x402b4495
    QUALNAME = "types.InputMessageReadMetric"

    def __init__(self, *, msg_id: int, view_id: int, time_in_view_ms: int, active_time_in_view_ms: int, height_to_viewport_ratio_permille: int, seen_range_ratio_permille: int) -> None:
        self.msg_id = msg_id  # int
        self.view_id = view_id  # long
        self.time_in_view_ms = time_in_view_ms  # int
        self.active_time_in_view_ms = active_time_in_view_ms  # int
        self.height_to_viewport_ratio_permille = height_to_viewport_ratio_permille  # int
        self.seen_range_ratio_permille = seen_range_ratio_permille  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputMessageReadMetric:
        # No flags
        
        msg_id = Int.read(b)
        
        view_id = Long.read(b)
        
        time_in_view_ms = Int.read(b)
        
        active_time_in_view_ms = Int.read(b)
        
        height_to_viewport_ratio_permille = Int.read(b)
        
        seen_range_ratio_permille = Int.read(b)
        
        return InputMessageReadMetric(msg_id=msg_id, view_id=view_id, time_in_view_ms=time_in_view_ms, active_time_in_view_ms=active_time_in_view_ms, height_to_viewport_ratio_permille=height_to_viewport_ratio_permille, seen_range_ratio_permille=seen_range_ratio_permille)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.msg_id))
        
        b.write(Long(self.view_id))
        
        b.write(Int(self.time_in_view_ms))
        
        b.write(Int(self.active_time_in_view_ms))
        
        b.write(Int(self.height_to_viewport_ratio_permille))
        
        b.write(Int(self.seen_range_ratio_permille))
        
        return b.getvalue()
