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


class MessageMediaPoll(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.MessageMedia`.

    Details:
        - Layer: ``229``
        - ID: ``773F4E66``

    Parameters:
        poll (:obj:`Poll <stdgram.raw.base.Poll>`):
            N/A

        results (:obj:`PollResults <stdgram.raw.base.PollResults>`):
            N/A

        attached_media (:obj:`MessageMedia <stdgram.raw.base.MessageMedia>`, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: list[str] = ["poll", "results", "attached_media"]

    ID = 0x773f4e66
    QUALNAME = "types.MessageMediaPoll"

    def __init__(self, *, poll: raw.base.Poll, results: raw.base.PollResults, attached_media: raw.base.MessageMedia | None = None) -> None:
        self.poll = poll  # Poll
        self.results = results  # PollResults
        self.attached_media = attached_media  # flags.0?MessageMedia

    @staticmethod
    def read(b: BytesIO, *args: Any) -> MessageMediaPoll:
        
        flags = Int.read(b)
        
        poll = TLObject.read(b)
        
        results = TLObject.read(b)
        
        attached_media = TLObject.read(b) if flags & (1 << 0) else None
        
        return MessageMediaPoll(poll=poll, results=results, attached_media=attached_media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.attached_media is not None else 0
        b.write(Int(flags))
        
        b.write(self.poll.write())
        
        b.write(self.results.write())
        
        if self.attached_media is not None:
            b.write(self.attached_media.write())
        
        return b.getvalue()
