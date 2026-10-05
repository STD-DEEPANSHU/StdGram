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


class InputMediaPhoto(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.InputMedia`.

    Details:
        - Layer: ``229``
        - ID: ``E3AF4434``

    Parameters:
        id (:obj:`InputPhoto <stdgram.raw.base.InputPhoto>`):
            N/A

        spoiler (``bool``, *optional*):
            N/A

        live_photo (``bool``, *optional*):
            N/A

        ttl_seconds (``int`` ``32-bit``, *optional*):
            N/A

        video (:obj:`InputDocument <stdgram.raw.base.InputDocument>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["id", "spoiler", "live_photo", "ttl_seconds", "video"]

    ID = 0xe3af4434
    QUALNAME = "types.InputMediaPhoto"

    def __init__(self, *, id: raw.base.InputPhoto, spoiler: bool | None = None, live_photo: bool | None = None, ttl_seconds: int | None = None, video: raw.base.InputDocument | None = None) -> None:
        self.id = id  # InputPhoto
        self.spoiler = spoiler  # flags.1?true
        self.live_photo = live_photo  # flags.2?true
        self.ttl_seconds = ttl_seconds  # flags.0?int
        self.video = video  # flags.2?InputDocument

    @staticmethod
    def read(b: BytesIO, *args: Any) -> InputMediaPhoto:
        
        flags = Int.read(b)
        
        spoiler = True if flags & (1 << 1) else False
        live_photo = True if flags & (1 << 2) else False
        id = TLObject.read(b)
        
        ttl_seconds = Int.read(b) if flags & (1 << 0) else None
        video = TLObject.read(b) if flags & (1 << 2) else None
        
        return InputMediaPhoto(id=id, spoiler=spoiler, live_photo=live_photo, ttl_seconds=ttl_seconds, video=video)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.spoiler else 0
        flags |= (1 << 2) if self.live_photo else 0
        flags |= (1 << 0) if self.ttl_seconds is not None else 0
        flags |= (1 << 2) if self.video is not None else 0
        b.write(Int(flags))
        
        b.write(self.id.write())
        
        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))
        
        if self.video is not None:
            b.write(self.video.write())
        
        return b.getvalue()
