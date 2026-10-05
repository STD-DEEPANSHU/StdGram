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


class UploadImportedMedia(TLObject["raw.base.MessageMedia"]):
    """Telegram API function.

    Details:
        - Layer: ``229``
        - ID: ``2A862092``

    Parameters:
        peer (:obj:`InputPeer <stdgram.raw.base.InputPeer>`):
            N/A

        import_id (``int`` ``64-bit``):
            N/A

        file_name (``str``):
            N/A

        media (:obj:`InputMedia <stdgram.raw.base.InputMedia>`):
            N/A

    Returns:
        :obj:`MessageMedia <stdgram.raw.base.MessageMedia>`
    """

    __slots__: list[str] = ["peer", "import_id", "file_name", "media"]

    ID = 0x2a862092
    QUALNAME = "functions.messages.UploadImportedMedia"

    def __init__(self, *, peer: raw.base.InputPeer, import_id: int, file_name: str, media: raw.base.InputMedia) -> None:
        self.peer = peer  # InputPeer
        self.import_id = import_id  # long
        self.file_name = file_name  # string
        self.media = media  # InputMedia

    @staticmethod
    def read(b: BytesIO, *args: Any) -> UploadImportedMedia:
        # No flags
        
        peer = TLObject.read(b)
        
        import_id = Long.read(b)
        
        file_name = String.read(b)
        
        media = TLObject.read(b)
        
        return UploadImportedMedia(peer=peer, import_id=import_id, file_name=file_name, media=media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Long(self.import_id))
        
        b.write(String(self.file_name))
        
        b.write(self.media.write())
        
        return b.getvalue()
