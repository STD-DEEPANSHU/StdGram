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


class UpdateGroupCallParticipants(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.Update`.

    Details:
        - Layer: ``229``
        - ID: ``F2EBDB4E``

    Parameters:
        call (:obj:`InputGroupCall <stdgram.raw.base.InputGroupCall>`):
            N/A

        participants (List of :obj:`GroupCallParticipant <stdgram.raw.base.GroupCallParticipant>`):
            N/A

        version (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["call", "participants", "version"]

    ID = 0xf2ebdb4e
    QUALNAME = "types.UpdateGroupCallParticipants"

    def __init__(self, *, call: raw.base.InputGroupCall, participants: list[raw.base.GroupCallParticipant], version: int) -> None:
        self.call = call  # InputGroupCall
        self.participants = participants  # Vector<GroupCallParticipant>
        self.version = version  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateGroupCallParticipants:
        # No flags
        
        call = TLObject.read(b)
        
        participants = TLObject.read(b)
        
        version = Int.read(b)
        
        return UpdateGroupCallParticipants(call=call, participants=participants, version=version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.call.write())
        
        b.write(Vector(self.participants))
        
        b.write(Int(self.version))
        
        return b.getvalue()
