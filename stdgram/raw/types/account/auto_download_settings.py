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


class AutoDownloadSettings(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.account.AutoDownloadSettings`.

    Details:
        - Layer: ``229``
        - ID: ``63CACF26``

    Parameters:
        low (:obj:`AutoDownloadSettings <stdgram.raw.base.AutoDownloadSettings>`):
            N/A

        medium (:obj:`AutoDownloadSettings <stdgram.raw.base.AutoDownloadSettings>`):
            N/A

        high (:obj:`AutoDownloadSettings <stdgram.raw.base.AutoDownloadSettings>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetAutoDownloadSettings
    """

    __slots__: list[str] = ["low", "medium", "high"]

    ID = 0x63cacf26
    QUALNAME = "types.account.AutoDownloadSettings"

    def __init__(self, *, low: raw.base.AutoDownloadSettings, medium: raw.base.AutoDownloadSettings, high: raw.base.AutoDownloadSettings) -> None:
        self.low = low  # AutoDownloadSettings
        self.medium = medium  # AutoDownloadSettings
        self.high = high  # AutoDownloadSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> AutoDownloadSettings:
        # No flags
        
        low = TLObject.read(b)
        
        medium = TLObject.read(b)
        
        high = TLObject.read(b)
        
        return AutoDownloadSettings(low=low, medium=medium, high=high)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.low.write())
        
        b.write(self.medium.write())
        
        b.write(self.high.write())
        
        return b.getvalue()
