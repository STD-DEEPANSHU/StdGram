#  StdGram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present <https://github.com/TelegramPlayGround>
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

import stdgram
from stdgram import enums, raw, types, utils

from ..object import Object

if TYPE_CHECKING:
    from datetime import datetime


class MessageOrigin(Object):
    """This object describes the origin of a message.

    It can be one of:

    - :obj:`~stdgram.types.MessageOriginChannel`
    - :obj:`~stdgram.types.MessageOriginChat`
    - :obj:`~stdgram.types.MessageOriginHiddenUser`
    - :obj:`~stdgram.types.MessageOriginImport`
    - :obj:`~stdgram.types.MessageOriginUser`
    """

    def __init__(self, type: enums.MessageOriginType, date: datetime | None = None):
        super().__init__()

        self.type = type
        self.date = date

    @staticmethod
    async def _parse(
        client: stdgram.Client,
        fwd_from: raw.types.MessageFwdHeader,
        users: dict[int, raw.base.User],
        chats: dict[int, raw.base.Chat],
    ) -> MessageOrigin | None:
        if not fwd_from:
            return None

        forward_date = utils.timestamp_to_datetime(fwd_from.date)

        if fwd_from.from_id:
            raw_peer_id = utils.get_raw_peer_id(fwd_from.from_id)
            peer_id = utils.get_peer_id(fwd_from.from_id)
            peer_type = utils.get_peer_type(peer_id)

            if peer_type == "user":
                return types.MessageOriginUser(
                    date=forward_date,
                    sender_user=await types.User._parse(client, users.get(raw_peer_id)),
                )
            else:
                if fwd_from.channel_post:
                    return types.MessageOriginChannel(
                        date=forward_date,
                        chat=await types.Chat._parse_channel_chat(client, chats.get(raw_peer_id)),
                        message_id=fwd_from.channel_post,
                        author_signature=fwd_from.post_author,
                    )
                else:
                    return types.MessageOriginChat(
                        date=forward_date,
                        sender_chat=await types.Chat._parse_channel_chat(
                            client, chats.get(raw_peer_id)
                        ),
                        author_signature=fwd_from.post_author,
                    )
        elif fwd_from.from_name:
            return types.MessageOriginHiddenUser(
                date=forward_date, sender_user_name=fwd_from.from_name
            )
        elif fwd_from.imported:
            return types.MessageOriginImport(
                date=forward_date, sender_user_name=fwd_from.post_author
            )
