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

import stdgram
from stdgram import raw, types

from ..object import Object


class GiftAuctionState(Object):
    """Represent auction state of a gift.

    Parameters:
        gift (:obj:`~stdgram.types.Gift`):
            The gift.

        state (:obj:`~stdgram.types.AuctionState`):
            Auction state of the gift.

        raw (:obj:`~stdgram.raw.base.StarGiftAuctionState`, *optional*):
            The raw object as received from the server.
    """

    def __init__(
        self,
        *,
        gift: types.Gift,
        state: types.AuctionState,
        raw: raw.base.StarGiftAuctionState | None = None,
    ):
        super().__init__()

        self.gift = gift
        self.state = state
        self.raw = raw

    @staticmethod
    async def _parse(
        client: stdgram.Client, gift_auction_state: raw.base.StarGiftAuctionState
    ) -> GiftAuctionState:
        state = None

        if isinstance(gift_auction_state.state, raw.types.StarGiftAuctionState):
            state = await types.AuctionStateActive._parse(gift_auction_state.state)
        elif isinstance(gift_auction_state.state, raw.types.StarGiftAuctionStateFinished):
            state = await types.AuctionStateFinished._parse(gift_auction_state.state)

        return GiftAuctionState(
            gift=await types.Gift._parse(client, gift_auction_state.gift),
            state=state,
            raw=gift_auction_state,
        )
