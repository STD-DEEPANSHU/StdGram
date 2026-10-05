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


class GroupCallParticipantVideo(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.GroupCallParticipantVideo`.

    Details:
        - Layer: ``229``
        - ID: ``67753AC8``

    Parameters:
        endpoint (``str``):
            N/A

        source_groups (List of :obj:`GroupCallParticipantVideoSourceGroup <stdgram.raw.base.GroupCallParticipantVideoSourceGroup>`):
            N/A

        paused (``bool``, *optional*):
            N/A

        audio_source (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: list[str] = ["endpoint", "source_groups", "paused", "audio_source"]

    ID = 0x67753ac8
    QUALNAME = "types.GroupCallParticipantVideo"

    def __init__(self, *, endpoint: str, source_groups: list[raw.base.GroupCallParticipantVideoSourceGroup], paused: bool | None = None, audio_source: int | None = None) -> None:
        self.endpoint = endpoint  # string
        self.source_groups = source_groups  # Vector<GroupCallParticipantVideoSourceGroup>
        self.paused = paused  # flags.0?true
        self.audio_source = audio_source  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GroupCallParticipantVideo:
        
        flags = Int.read(b)
        
        paused = True if flags & (1 << 0) else False
        endpoint = String.read(b)
        
        source_groups = TLObject.read(b)
        
        audio_source = Int.read(b) if flags & (1 << 1) else None
        return GroupCallParticipantVideo(endpoint=endpoint, source_groups=source_groups, paused=paused, audio_source=audio_source)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.paused else 0
        flags |= (1 << 1) if self.audio_source is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.endpoint))
        
        b.write(Vector(self.source_groups))
        
        if self.audio_source is not None:
            b.write(Int(self.audio_source))
        
        return b.getvalue()
