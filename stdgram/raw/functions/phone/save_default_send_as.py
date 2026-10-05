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


class SaveDefaultSendAs(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``4167ADD1``

    Parameters:
        call (:obj:`InputGroupCall <stdgram.raw.base.InputGroupCall>`):
            N/A

        send_as (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["call", "send_as"]

    ID = 0x4167add1
    QUALNAME = "functions.phone.SaveDefaultSendAs"

    def __init__(self, *, call: raw.base.InputGroupCall, send_as: raw.base.InputPeer) -> None:
        self.call = call  # InputGroupCall
        self.send_as = send_as  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SaveDefaultSendAs:
        # No flags
        
        call = TLObject.read(b)
        
        send_as = TLObject.read(b)
        
        return SaveDefaultSendAs(call=call, send_as=send_as)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.call.write())
        
        b.write(self.send_as.write())
        
        return b.getvalue()
