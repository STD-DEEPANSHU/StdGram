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


class DeleteConferenceCallParticipants(TLObject["raw.base.Updates"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``8CA60525``

    Parameters:
        call (:obj:`InputGroupCall <stdgram.raw.base.InputGroupCall>`):
            N/A

        ids (List of ``int`` ``64-bit``):
            N/A

        block (``bytes``):
            N/A

        only_left (``bool``, *optional*):
            N/A

        kick (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <stdgram.raw.base.Updates>`
    """

    __slots__: list[str] = ["call", "ids", "block", "only_left", "kick"]

    ID = 0x8ca60525
    QUALNAME = "functions.phone.DeleteConferenceCallParticipants"

    def __init__(self, *, call: raw.base.InputGroupCall, ids: list[int], block: bytes, only_left: bool | None = None, kick: bool | None = None) -> None:
        self.call = call  # InputGroupCall
        self.ids = ids  # Vector<long>
        self.block = block  # bytes
        self.only_left = only_left  # flags.0?true
        self.kick = kick  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> DeleteConferenceCallParticipants:
        
        flags = Int.read(b)
        
        only_left = True if flags & (1 << 0) else False
        kick = True if flags & (1 << 1) else False
        call = TLObject.read(b)
        
        ids = TLObject.read(b, Long)
        
        block = Bytes.read(b)
        
        return DeleteConferenceCallParticipants(call=call, ids=ids, block=block, only_left=only_left, kick=kick)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.only_left else 0
        flags |= (1 << 1) if self.kick else 0
        b.write(Int(flags))
        
        b.write(self.call.write())
        
        b.write(Vector(self.ids, Long))
        
        b.write(Bytes(self.block))
        
        return b.getvalue()
