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


class DeleteGroupCallParticipantMessages(TLObject["raw.base.Updates"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``1DBFECA0``

    Parameters:
        call (:obj:`InputGroupCall <stdgram.raw.base.InputGroupCall>`):
            N/A

        participant (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        report_spam (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <stdgram.raw.base.Updates>`
    """

    __slots__: list[str] = ["call", "participant", "report_spam"]

    ID = 0x1dbfeca0
    QUALNAME = "functions.phone.DeleteGroupCallParticipantMessages"

    def __init__(self, *, call: raw.base.InputGroupCall, participant: raw.base.InputPeer, report_spam: bool | None = None) -> None:
        self.call = call  # InputGroupCall
        self.participant = participant  # InputPeer
        self.report_spam = report_spam  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> DeleteGroupCallParticipantMessages:
        
        flags = Int.read(b)
        
        report_spam = True if flags & (1 << 0) else False
        call = TLObject.read(b)
        
        participant = TLObject.read(b)
        
        return DeleteGroupCallParticipantMessages(call=call, participant=participant, report_spam=report_spam)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.report_spam else 0
        b.write(Int(flags))
        
        b.write(self.call.write())
        
        b.write(self.participant.write())
        
        return b.getvalue()
