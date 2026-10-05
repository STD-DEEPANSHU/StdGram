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


class InputMediaPoll(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputMedia`.

    Details:
        - Layer: ``229``
        - ID: ``883A4108``

    Parameters:
        poll (:obj:`Poll <stdgram.raw.base.Poll>`):
            N/A

        correct_answers (List of ``int`` ``32-bit``, *optional*):
            N/A

        attached_media (:obj:`InputMedia <stdgram.raw.base.InputMedia>`, *optional*):
            N/A

        solution (``str``, *optional*):
            N/A

        solution_entities (List of :obj:`MessageEntity <stdgram.raw.base.MessageEntity>`, *optional*):
            N/A

        solution_media (:obj:`InputMedia <stdgram.raw.base.InputMedia>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["poll", "correct_answers", "attached_media", "solution", "solution_entities", "solution_media"]

    ID = 0x883a4108
    QUALNAME = "types.InputMediaPoll"

    def __init__(self, *, poll: raw.base.Poll, correct_answers: list[int] | None = None, attached_media: raw.base.InputMedia | None = None, solution: str | None = None, solution_entities: list[raw.base.MessageEntity] | None = None, solution_media: raw.base.InputMedia | None = None) -> None:
        self.poll = poll  # Poll
        self.correct_answers = correct_answers  # flags.0?Vector<int>
        self.attached_media = attached_media  # flags.3?InputMedia
        self.solution = solution  # flags.1?string
        self.solution_entities = solution_entities  # flags.1?Vector<MessageEntity>
        self.solution_media = solution_media  # flags.2?InputMedia

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputMediaPoll:
        
        flags = Int.read(b)
        
        poll = TLObject.read(b)
        
        correct_answers = TLObject.read(b, Int) if flags & (1 << 0) else []
        
        attached_media = TLObject.read(b) if flags & (1 << 3) else None
        
        solution = String.read(b) if flags & (1 << 1) else None
        solution_entities = TLObject.read(b) if flags & (1 << 1) else []
        
        solution_media = TLObject.read(b) if flags & (1 << 2) else None
        
        return InputMediaPoll(poll=poll, correct_answers=correct_answers, attached_media=attached_media, solution=solution, solution_entities=solution_entities, solution_media=solution_media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.correct_answers else 0
        flags |= (1 << 3) if self.attached_media is not None else 0
        flags |= (1 << 1) if self.solution is not None else 0
        flags |= (1 << 1) if self.solution_entities else 0
        flags |= (1 << 2) if self.solution_media is not None else 0
        b.write(Int(flags))
        
        b.write(self.poll.write())
        
        if self.correct_answers is not None:
            b.write(Vector(self.correct_answers, Int))
        
        if self.attached_media is not None:
            b.write(self.attached_media.write())
        
        if self.solution is not None:
            b.write(String(self.solution))
        
        if self.solution_entities is not None:
            b.write(Vector(self.solution_entities))
        
        if self.solution_media is not None:
            b.write(self.solution_media.write())
        
        return b.getvalue()
