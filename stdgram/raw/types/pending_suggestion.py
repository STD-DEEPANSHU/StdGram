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


class PendingSuggestion(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.PendingSuggestion`.

    Details:
        - Layer: ``229``
        - ID: ``E7E82E12``

    Parameters:
        suggestion (``str``):
            N/A

        title (:obj:`TextWithEntities <stdgram.raw.base.TextWithEntities>`):
            N/A

        description (:obj:`TextWithEntities <stdgram.raw.base.TextWithEntities>`):
            N/A

        url (``str``):
            N/A

    """

    __slots__: list[str] = ["suggestion", "title", "description", "url"]

    ID = 0xe7e82e12
    QUALNAME = "types.PendingSuggestion"

    def __init__(self, *, suggestion: str, title: raw.base.TextWithEntities, description: raw.base.TextWithEntities, url: str) -> None:
        self.suggestion = suggestion  # string
        self.title = title  # TextWithEntities
        self.description = description  # TextWithEntities
        self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> PendingSuggestion:
        # No flags
        
        suggestion = String.read(b)
        
        title = TLObject.read(b)
        
        description = TLObject.read(b)
        
        url = String.read(b)
        
        return PendingSuggestion(suggestion=suggestion, title=title, description=description, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.suggestion))
        
        b.write(self.title.write())
        
        b.write(self.description.write())
        
        b.write(String(self.url))
        
        return b.getvalue()
