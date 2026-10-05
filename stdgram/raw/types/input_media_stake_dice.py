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


class InputMediaStakeDice(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputMedia`.

    Details:
        - Layer: ``229``
        - ID: ``F3A9244A``

    Parameters:
        game_hash (``str``):
            N/A

        ton_amount (``int`` ``64-bit``):
            N/A

        client_seed (``bytes``):
            N/A

    """

    __slots__: list[str] = ["game_hash", "ton_amount", "client_seed"]

    ID = 0xf3a9244a
    QUALNAME = "types.InputMediaStakeDice"

    def __init__(self, *, game_hash: str, ton_amount: int, client_seed: bytes) -> None:
        self.game_hash = game_hash  # string
        self.ton_amount = ton_amount  # long
        self.client_seed = client_seed  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputMediaStakeDice:
        # No flags
        
        game_hash = String.read(b)
        
        ton_amount = Long.read(b)
        
        client_seed = Bytes.read(b)
        
        return InputMediaStakeDice(game_hash=game_hash, ton_amount=ton_amount, client_seed=client_seed)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.game_hash))
        
        b.write(Long(self.ton_amount))
        
        b.write(Bytes(self.client_seed))
        
        return b.getvalue()
