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


class MessageReportOption(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.MessageReportOption`.

    Details:
        - Layer: ``229``
        - ID: ``7903E3D9``

    Parameters:
        text (``str``):
            N/A

        option (``bytes``):
            N/A

    """

    __slots__: list[str] = ["text", "option"]

    ID = 0x7903e3d9
    QUALNAME = "types.MessageReportOption"

    def __init__(self, *, text: str, option: bytes) -> None:
        self.text = text  # string
        self.option = option  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> MessageReportOption:
        # No flags
        
        text = String.read(b)
        
        option = Bytes.read(b)
        
        return MessageReportOption(text=text, option=option)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.text))
        
        b.write(Bytes(self.option))
        
        return b.getvalue()
