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


class GetAdminedPublicChannels(TLObject["raw.base.messages.Chats"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``F8B036AF``

    Parameters:
        by_location (``bool``, *optional*):
            N/A

        check_limit (``bool``, *optional*):
            N/A

        for_personal (``bool``, *optional*):
            N/A

        for_community_peer (``bool``, *optional*):
            N/A

    Returns:
        :obj:`messages.Chats <stdgram.raw.base.messages.Chats>`
    """

    __slots__: list[str] = ["by_location", "check_limit", "for_personal", "for_community_peer"]

    ID = 0xf8b036af
    QUALNAME = "functions.channels.GetAdminedPublicChannels"

    def __init__(self, *, by_location: bool | None = None, check_limit: bool | None = None, for_personal: bool | None = None, for_community_peer: bool | None = None) -> None:
        self.by_location = by_location  # flags.0?true
        self.check_limit = check_limit  # flags.1?true
        self.for_personal = for_personal  # flags.2?true
        self.for_community_peer = for_community_peer  # flags.3?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GetAdminedPublicChannels:
        
        flags = Int.read(b)
        
        by_location = True if flags & (1 << 0) else False
        check_limit = True if flags & (1 << 1) else False
        for_personal = True if flags & (1 << 2) else False
        for_community_peer = True if flags & (1 << 3) else False
        return GetAdminedPublicChannels(by_location=by_location, check_limit=check_limit, for_personal=for_personal, for_community_peer=for_community_peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.by_location else 0
        flags |= (1 << 1) if self.check_limit else 0
        flags |= (1 << 2) if self.for_personal else 0
        flags |= (1 << 3) if self.for_community_peer else 0
        b.write(Int(flags))
        
        return b.getvalue()
