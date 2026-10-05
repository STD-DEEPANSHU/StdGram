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


class GetPremiumGiftCodeOptions(TLObject["list[raw.base.PremiumGiftCodeOption]"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``2757BA54``

    Parameters:
        boost_peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`, *optional*):
            N/A

    Returns:
        List of :obj:`PremiumGiftCodeOption <stdgram.raw.base.PremiumGiftCodeOption>`
    """

    __slots__: list[str] = ["boost_peer"]

    ID = 0x2757ba54
    QUALNAME = "functions.payments.GetPremiumGiftCodeOptions"

    def __init__(self, *, boost_peer: raw.base.InputPeer | None = None) -> None:
        self.boost_peer = boost_peer  # flags.0?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GetPremiumGiftCodeOptions:
        
        flags = Int.read(b)
        
        boost_peer = TLObject.read(b) if flags & (1 << 0) else None
        
        return GetPremiumGiftCodeOptions(boost_peer=boost_peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.boost_peer is not None else 0
        b.write(Int(flags))
        
        if self.boost_peer is not None:
            b.write(self.boost_peer.write())
        
        return b.getvalue()
