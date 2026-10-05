#  StdGram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
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
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with StdGram.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import annotations as _annotations

from typing import TYPE_CHECKING
from uuid import uuid4

from ..object import Object

if TYPE_CHECKING:
    import stdgram
    from stdgram import types


class InlineQueryResult(Object):
    """One result of an inline query.

    - :obj:`~stdgram.types.InlineQueryResultCachedAudio`
    - :obj:`~stdgram.types.InlineQueryResultCachedDocument`
    - :obj:`~stdgram.types.InlineQueryResultCachedAnimation`
    - :obj:`~stdgram.types.InlineQueryResultCachedPhoto`
    - :obj:`~stdgram.types.InlineQueryResultCachedSticker`
    - :obj:`~stdgram.types.InlineQueryResultCachedVideo`
    - :obj:`~stdgram.types.InlineQueryResultCachedVoice`
    - :obj:`~stdgram.types.InlineQueryResultArticle`
    - :obj:`~stdgram.types.InlineQueryResultAudio`
    - :obj:`~stdgram.types.InlineQueryResultContact`
    - :obj:`~stdgram.types.InlineQueryResultDocument`
    - :obj:`~stdgram.types.InlineQueryResultAnimation`
    - :obj:`~stdgram.types.InlineQueryResultLocation`
    - :obj:`~stdgram.types.InlineQueryResultPhoto`
    - :obj:`~stdgram.types.InlineQueryResultVenue`
    - :obj:`~stdgram.types.InlineQueryResultVideo`
    - :obj:`~stdgram.types.InlineQueryResultVoice`
    """

    def __init__(
        self,
        type: str,
        id: str,
        input_message_content: types.InputMessageContent,
        reply_markup: types.InlineKeyboardMarkup,
    ):
        super().__init__()

        self.type = type
        self.id = str(uuid4()) if id is None else str(id)
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup

    async def write(self, client: stdgram.Client):
        pass
