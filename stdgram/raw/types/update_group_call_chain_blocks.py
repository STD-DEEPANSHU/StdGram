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


class UpdateGroupCallChainBlocks(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.Update`.

    Details:
        - Layer: ``229``
        - ID: ``A477288F``

    Parameters:
        call (:obj:`InputGroupCall <stdgram.raw.base.InputGroupCall>`):
            N/A

        sub_chain_id (``int`` ``32-bit``):
            N/A

        blocks (List of ``bytes``):
            N/A

        next_offset (``int`` ``32-bit``):
            N/A

    """

    __slots__: list[str] = ["call", "sub_chain_id", "blocks", "next_offset"]

    ID = 0xa477288f
    QUALNAME = "types.UpdateGroupCallChainBlocks"

    def __init__(self, *, call: raw.base.InputGroupCall, sub_chain_id: int, blocks: list[bytes], next_offset: int) -> None:
        self.call = call  # InputGroupCall
        self.sub_chain_id = sub_chain_id  # int
        self.blocks = blocks  # Vector<bytes>
        self.next_offset = next_offset  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateGroupCallChainBlocks:
        # No flags
        
        call = TLObject.read(b)
        
        sub_chain_id = Int.read(b)
        
        blocks = TLObject.read(b, Bytes)
        
        next_offset = Int.read(b)
        
        return UpdateGroupCallChainBlocks(call=call, sub_chain_id=sub_chain_id, blocks=blocks, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.call.write())
        
        b.write(Int(self.sub_chain_id))
        
        b.write(Vector(self.blocks, Bytes))
        
        b.write(Int(self.next_offset))
        
        return b.getvalue()
