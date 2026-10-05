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


class ToggleSignatures(TLObject["raw.base.Updates"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``418D549C``

    Parameters:
        channel (:obj:`InputChannel <stdgram.raw.base.InputChannel>`):
            N/A

        signatures_enabled (``bool``, *optional*):
            N/A

        profiles_enabled (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <stdgram.raw.base.Updates>`
    """

    __slots__: list[str] = ["channel", "signatures_enabled", "profiles_enabled"]

    ID = 0x418d549c
    QUALNAME = "functions.channels.ToggleSignatures"

    def __init__(self, *, channel: raw.base.InputChannel, signatures_enabled: bool | None = None, profiles_enabled: bool | None = None) -> None:
        self.channel = channel  # InputChannel
        self.signatures_enabled = signatures_enabled  # flags.0?true
        self.profiles_enabled = profiles_enabled  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> ToggleSignatures:
        
        flags = Int.read(b)
        
        signatures_enabled = True if flags & (1 << 0) else False
        profiles_enabled = True if flags & (1 << 1) else False
        channel = TLObject.read(b)
        
        return ToggleSignatures(channel=channel, signatures_enabled=signatures_enabled, profiles_enabled=profiles_enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.signatures_enabled else 0
        flags |= (1 << 1) if self.profiles_enabled else 0
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        return b.getvalue()
