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


class WebBrowserSettings(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.account.WebBrowserSettings`.

    Details:
        - Layer: ``229``
        - ID: ``79EB8CB3``

    Parameters:
        external_exceptions (List of :obj:`WebDomainException <stdgram.raw.base.WebDomainException>`):
            N/A

        inapp_exceptions (List of :obj:`WebDomainException <stdgram.raw.base.WebDomainException>`):
            N/A

        hash (``int`` ``64-bit``):
            N/A

        open_external_browser (``bool``, *optional*):
            N/A

        display_close_button (``bool``, *optional*):
            N/A

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetWebBrowserSettings
            account.UpdateWebBrowserSettings
            account.DeleteWebBrowserSettingsExceptions
    """

    __slots__: list[str] = ["external_exceptions", "inapp_exceptions", "hash", "open_external_browser", "display_close_button"]

    ID = 0x79eb8cb3
    QUALNAME = "types.account.WebBrowserSettings"

    def __init__(self, *, external_exceptions: list[raw.base.WebDomainException], inapp_exceptions: list[raw.base.WebDomainException], hash: int, open_external_browser: bool | None = None, display_close_button: bool | None = None) -> None:
        self.external_exceptions = external_exceptions  # Vector<WebDomainException>
        self.inapp_exceptions = inapp_exceptions  # Vector<WebDomainException>
        self.hash = hash  # long
        self.open_external_browser = open_external_browser  # flags.0?true
        self.display_close_button = display_close_button  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> WebBrowserSettings:
        
        flags = Int.read(b)
        
        open_external_browser = True if flags & (1 << 0) else False
        display_close_button = True if flags & (1 << 1) else False
        external_exceptions = TLObject.read(b)
        
        inapp_exceptions = TLObject.read(b)
        
        hash = Long.read(b)
        
        return WebBrowserSettings(external_exceptions=external_exceptions, inapp_exceptions=inapp_exceptions, hash=hash, open_external_browser=open_external_browser, display_close_button=display_close_button)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.open_external_browser else 0
        flags |= (1 << 1) if self.display_close_button else 0
        b.write(Int(flags))
        
        b.write(Vector(self.external_exceptions))
        
        b.write(Vector(self.inapp_exceptions))
        
        b.write(Long(self.hash))
        
        return b.getvalue()
