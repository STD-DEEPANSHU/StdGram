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


class SummarizeText(TLObject["raw.base.TextWithEntities"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``ABBBD346``

    Parameters:
        peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        id (``int`` ``32-bit``):
            N/A

        to_lang (``str``, *optional*):
            N/A

        tone (``str``, *optional*):
            N/A

    Returns:
        :obj:`TextWithEntities <stdgram.raw.base.TextWithEntities>`
    """

    __slots__: list[str] = ["peer", "id", "to_lang", "tone"]

    ID = 0xabbbd346
    QUALNAME = "functions.messages.SummarizeText"

    def __init__(self, *, peer: raw.base.InputPeer, id: int, to_lang: str | None = None, tone: str | None = None) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.to_lang = to_lang  # flags.0?string
        self.tone = tone  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> SummarizeText:
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        id = Int.read(b)
        
        to_lang = String.read(b) if flags & (1 << 0) else None
        tone = String.read(b) if flags & (1 << 2) else None
        return SummarizeText(peer=peer, id=id, to_lang=to_lang, tone=tone)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.to_lang is not None else 0
        flags |= (1 << 2) if self.tone is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        if self.to_lang is not None:
            b.write(String(self.to_lang))
        
        if self.tone is not None:
            b.write(String(self.tone))
        
        return b.getvalue()
