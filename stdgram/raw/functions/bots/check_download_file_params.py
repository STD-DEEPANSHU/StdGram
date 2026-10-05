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


class CheckDownloadFileParams(TLObject["bool"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``50077589``

    Parameters:
        bot (:obj:`InputUser <stdgram.raw.base.InputUser>`):
            N/A

        file_name (``str``):
            N/A

        url (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: list[str] = ["bot", "file_name", "url"]

    ID = 0x50077589
    QUALNAME = "functions.bots.CheckDownloadFileParams"

    def __init__(self, *, bot: raw.base.InputUser, file_name: str, url: str) -> None:
        self.bot = bot  # InputUser
        self.file_name = file_name  # string
        self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> CheckDownloadFileParams:
        # No flags
        
        bot = TLObject.read(b)
        
        file_name = String.read(b)
        
        url = String.read(b)
        
        return CheckDownloadFileParams(bot=bot, file_name=file_name, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot.write())
        
        b.write(String(self.file_name))
        
        b.write(String(self.url))
        
        return b.getvalue()
