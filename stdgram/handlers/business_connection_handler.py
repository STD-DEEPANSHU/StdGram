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

from stdgram import types

from .handler import Handler

if TYPE_CHECKING:
    import stdgram
    from stdgram.filters import Filter

BusinessConnectionCallbackType = Callable[["stdgram.Client", types.BusinessConnection], Any]


class BusinessConnectionHandler(Handler[BusinessConnectionCallbackType]):
    """The BusinessConnection handler class. Used to handle changes in business connections.

    It is intended to be used with :meth:`~stdgram.Client.add_handler`

    For a nicer way to register this handler, have a look at the
    :meth:`~stdgram.Client.on_business_connection` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a business connection has changed. It takes *(client, update)*
            as positional arguments (look at the section below for a detailed description).

        filters (:obj:`~stdgram.filters.Filter`):
            Pass one or more filters to allow only a subset of updates to be passed
            in your callback function.

    Other parameters:
        client (:obj:`~stdgram.Client`):
            The Client itself, useful when you want to call other API methods inside the handler.

        update (:obj:`~stdgram.types.BusinessConnection`):
            Information about business connection.
    """

    def __init__(
        self,
        callback: BusinessConnectionCallbackType,
        filters: Filter | None = None,
    ) -> None:
        super().__init__(callback, filters)
