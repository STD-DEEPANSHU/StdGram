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


class MessageMediaPaidMedia(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.MessageMedia`.

    Details:
        - Layer: ``229``
        - ID: ``A8852491``

    Parameters:
        stars_amount (``int`` ``64-bit``):
            N/A

        extended_media (List of :obj:`MessageExtendedMedia <stdgram.raw.base.MessageExtendedMedia>`):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: list[str] = ["stars_amount", "extended_media"]

    ID = 0xa8852491
    QUALNAME = "types.MessageMediaPaidMedia"

    def __init__(self, *, stars_amount: int, extended_media: list[raw.base.MessageExtendedMedia]) -> None:
        self.stars_amount = stars_amount  # long
        self.extended_media = extended_media  # Vector<MessageExtendedMedia>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> MessageMediaPaidMedia:
        # No flags
        
        stars_amount = Long.read(b)
        
        extended_media = TLObject.read(b)
        
        return MessageMediaPaidMedia(stars_amount=stars_amount, extended_media=extended_media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.stars_amount))
        
        b.write(Vector(self.extended_media))
        
        return b.getvalue()
