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


class TermsOfServiceUpdate(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.help.TermsOfServiceUpdate`.

    Details:
        - Layer: ``229``
        - ID: ``28ECF961``

    Parameters:
        expires (``int`` ``32-bit``):
            N/A

        terms_of_service (:obj:`help.TermsOfService <stdgram.raw.base.help.TermsOfService>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: stdgram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetTermsOfServiceUpdate
    """

    __slots__: list[str] = ["expires", "terms_of_service"]

    ID = 0x28ecf961
    QUALNAME = "types.help.TermsOfServiceUpdate"

    def __init__(self, *, expires: int, terms_of_service: raw.base.help.TermsOfService) -> None:
        self.expires = expires  # int
        self.terms_of_service = terms_of_service  # help.TermsOfService

    @staticmethod
    def read(b: BytesIO, *args: Any) -> TermsOfServiceUpdate:
        # No flags
        
        expires = Int.read(b)
        
        terms_of_service = TLObject.read(b)
        
        return TermsOfServiceUpdate(expires=expires, terms_of_service=terms_of_service)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.expires))
        
        b.write(self.terms_of_service.write())
        
        return b.getvalue()
