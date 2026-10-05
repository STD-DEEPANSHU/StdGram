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

from collections.abc import Callable
from typing import TYPE_CHECKING, Any

from stdgram import raw

from .handler import Handler

if TYPE_CHECKING:
    import stdgram
    from stdgram.filters import Filter

RawUpdateCallbackType = Callable[
    [
        "stdgram.Client",
        raw.base.Update,
        dict[int, raw.base.User],
        dict[int, raw.base.Chat],
    ],
    Any,
]


class RawUpdateHandler(Handler[RawUpdateCallbackType]):
    """The Raw Update handler class. Used to handle raw updates. It is intended to be used with
    :meth:`~stdgram.Client.add_handler`

    For a nicer way to register this handler, have a look at the
    :meth:`~stdgram.Client.on_raw_update` decorator.

    Parameters:
        callback (``Callable``):
            A function that will be called when a new update is received from the server. It takes
            *(client, update, users, chats)* as positional arguments (look at the section below for
            a detailed description).

        filters (:obj:`~stdgram.filters.Filter`):
            Pass one or more filters to allow only a subset of updates to be passed
            in your callback function.

    Other Parameters:
        client (:obj:`~stdgram.Client`):
            The Client itself, useful when you want to call other API methods inside the update handler.

        update (:obj:`~stdgram.raw.base.Update`):
            The received update, which can be one of the many single Updates listed in the
            :obj:`~stdgram.raw.base.Update` base type.

        users (``dict``):
            Dictionary of all :obj:`~stdgram.raw.base.User` mentioned in the update.
            You can access extra info about the user (such as *first_name*, *last_name*, etc...) by using
            the IDs you find in the *update* argument (e.g.: *users[1768841572]*).

        chats (``dict``):
            Dictionary of all :obj:`~stdgram.raw.base.Chat` mentioned in the update.
            You can access extra info about the chat (such as *title*, *participants_count*, etc...)
            by using the IDs you find in the *update* argument (e.g.: *chats[1701277281]*).

    .. note::

        The following Empty or Forbidden types may exist inside the *users* and *chats* dictionaries.
        They mean you have been blocked by the user or banned from the group/channel.

        - :obj:`~stdgram.raw.types.UserEmpty`
        - :obj:`~stdgram.raw.types.ChatEmpty`
        - :obj:`~stdgram.raw.types.ChatForbidden`
        - :obj:`~stdgram.raw.types.ChannelForbidden`
    """

    def __init__(self, callback: RawUpdateCallbackType, filters: Filter | None = None) -> None:
        super().__init__(callback, filters)
