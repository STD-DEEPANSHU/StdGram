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


class DeleteExportedInvite(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``719C5C5E``

    Parameters:
        chatlist (:obj:`InputChatlist <stdgram.raw.base.InputChatlist>`):
            N/A

        slug (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["chatlist", "slug"]

    ID = 0x719c5c5e
    QUALNAME = "functions.chatlists.DeleteExportedInvite"

    def __init__(self, *, chatlist: raw.base.InputChatlist, slug: str) -> None:
        self.chatlist = chatlist  # InputChatlist
        self.slug = slug  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> DeleteExportedInvite:
        # No flags
        
        chatlist = TLObject.read(b)
        
        slug = String.read(b)
        
        return DeleteExportedInvite(chatlist=chatlist, slug=slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.chatlist.write())
        
        b.write(String(self.slug))
        
        return b.getvalue()
