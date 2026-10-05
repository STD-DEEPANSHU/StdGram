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


class UpdateProfilePhoto(TLObject["raw.base.photos.Photo"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``9E82039``

    Parameters:
        id (:obj:`InputPhoto <stdgram.raw.base.InputPhoto>`):
            N/A

        fallback (``bool``, *optional*):
            N/A

        bot (:obj:`InputUser <stdgram.raw.base.InputUser>`, *optional*):
            N/A

    Returns:
        :obj:`photos.Photo <stdgram.raw.base.photos.Photo>`
    """

    __slots__: list[str] = ["id", "fallback", "bot"]

    ID = 0x9e82039
    QUALNAME = "functions.photos.UpdateProfilePhoto"

    def __init__(self, *, id: raw.base.InputPhoto, fallback: bool | None = None, bot: raw.base.InputUser | None = None) -> None:
        self.id = id  # InputPhoto
        self.fallback = fallback  # flags.0?true
        self.bot = bot  # flags.1?InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UpdateProfilePhoto:
        
        flags = Int.read(b)
        
        fallback = True if flags & (1 << 0) else False
        bot = TLObject.read(b) if flags & (1 << 1) else None
        
        id = TLObject.read(b)
        
        return UpdateProfilePhoto(id=id, fallback=fallback, bot=bot)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.fallback else 0
        flags |= (1 << 1) if self.bot is not None else 0
        b.write(Int(flags))
        
        if self.bot is not None:
            b.write(self.bot.write())
        
        b.write(self.id.write())
        
        return b.getvalue()
