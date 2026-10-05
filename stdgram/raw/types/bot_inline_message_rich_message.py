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


class BotInlineMessageRichMessage(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.BotInlineMessage`.

    Details:
        - Layer: ``229``
        - ID: ``A617E7B``

    Parameters:
        rich_message (:obj:`RichMessage <stdgram.raw.base.RichMessage>`):
            N/A

        reply_markup (:obj:`ReplyMarkup <stdgram.raw.base.ReplyMarkup>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["rich_message", "reply_markup"]

    ID = 0xa617e7b
    QUALNAME = "types.BotInlineMessageRichMessage"

    def __init__(self, *, rich_message: raw.base.RichMessage, reply_markup: raw.base.ReplyMarkup | None = None) -> None:
        self.rich_message = rich_message  # RichMessage
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup

    @staticmethod
    def read(b: BytesIO, *args: Any) -> BotInlineMessageRichMessage:
        
        flags = Int.read(b)
        
        reply_markup = TLObject.read(b) if flags & (1 << 2) else None
        
        rich_message = TLObject.read(b)
        
        return BotInlineMessageRichMessage(rich_message=rich_message, reply_markup=reply_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        b.write(Int(flags))
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        b.write(self.rich_message.write())
        
        return b.getvalue()
