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


class EmojiGameOutcome(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.messages.EmojiGameOutcome`.

    Details:
        - Layer: ``229``
        - ID: ``DA2AD647``

    Parameters:
        seed (``bytes``):
            N/A

        stake_ton_amount (``int`` ``64-bit``):
            N/A

        ton_amount (``int`` ``64-bit``):
            N/A

    """

    __slots__: list[str] = ["seed", "stake_ton_amount", "ton_amount"]

    ID = 0xda2ad647
    QUALNAME = "types.messages.EmojiGameOutcome"

    def __init__(self, *, seed: bytes, stake_ton_amount: int, ton_amount: int) -> None:
        self.seed = seed  # bytes
        self.stake_ton_amount = stake_ton_amount  # long
        self.ton_amount = ton_amount  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> EmojiGameOutcome:
        # No flags
        
        seed = Bytes.read(b)
        
        stake_ton_amount = Long.read(b)
        
        ton_amount = Long.read(b)
        
        return EmojiGameOutcome(seed=seed, stake_ton_amount=stake_ton_amount, ton_amount=ton_amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.seed))
        
        b.write(Long(self.stake_ton_amount))
        
        b.write(Long(self.ton_amount))
        
        return b.getvalue()
