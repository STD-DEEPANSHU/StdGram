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


class DeletePreviewMedia(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``2D0135B3``

    Parameters:
        bot (:obj:`InputUser <stdgram.raw.base.InputUser>`):
            N/A

        lang_code (``str``):
            N/A

        media (List of :obj:`InputMedia <stdgram.raw.base.InputMedia>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["bot", "lang_code", "media"]

    ID = 0x2d0135b3
    QUALNAME = "functions.bots.DeletePreviewMedia"

    def __init__(self, *, bot: raw.base.InputUser, lang_code: str, media: list[raw.base.InputMedia]) -> None:
        self.bot = bot  # InputUser
        self.lang_code = lang_code  # string
        self.media = media  # Vector<InputMedia>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> DeletePreviewMedia:
        # No flags
        
        bot = TLObject.read(b)
        
        lang_code = String.read(b)
        
        media = TLObject.read(b)
        
        return DeletePreviewMedia(bot=bot, lang_code=lang_code, media=media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot.write())
        
        b.write(String(self.lang_code))
        
        b.write(Vector(self.media))
        
        return b.getvalue()
