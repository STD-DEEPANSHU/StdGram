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


class GroupCall(TLObject):
    """Telegram API type.

    Constructor of :obj:`~stdgram.raw.base.GroupCall`.

    Details:
        - Layer: ``229``
        - ID: ``EFB2B617``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        access_hash (``int`` ``64-bit``):
            N/A

        participants_count (``int`` ``32-bit``):
            N/A

        unmuted_video_limit (``int`` ``32-bit``):
            N/A

        version (``int`` ``32-bit``):
            N/A

        join_muted (``bool``, *optional*):
            N/A

        can_change_join_muted (``bool``, *optional*):
            N/A

        join_date_asc (``bool``, *optional*):
            N/A

        schedule_start_subscribed (``bool``, *optional*):
            N/A

        can_start_video (``bool``, *optional*):
            N/A

        record_video_active (``bool``, *optional*):
            N/A

        rtmp_stream (``bool``, *optional*):
            N/A

        listeners_hidden (``bool``, *optional*):
            N/A

        conference (``bool``, *optional*):
            N/A

        creator (``bool``, *optional*):
            N/A

        messages_enabled (``bool``, *optional*):
            N/A

        can_change_messages_enabled (``bool``, *optional*):
            N/A

        min (``bool``, *optional*):
            N/A

        title (``str``, *optional*):
            N/A

        stream_dc_id (``int`` ``32-bit``, *optional*):
            N/A

        record_start_date (``int`` ``32-bit``, *optional*):
            N/A

        schedule_date (``int`` ``32-bit``, *optional*):
            N/A

        unmuted_video_count (``int`` ``32-bit``, *optional*):
            N/A

        invite_link (``str``, *optional*):
            N/A

        send_paid_messages_stars (``int`` ``64-bit``, *optional*):
            N/A

        default_send_as (:obj:`Peer <stdgram.raw.base.Peer>`, *optional*):
            N/A

    """

    __slots__: list[str] = ["id", "access_hash", "participants_count", "unmuted_video_limit", "version", "join_muted", "can_change_join_muted", "join_date_asc", "schedule_start_subscribed", "can_start_video", "record_video_active", "rtmp_stream", "listeners_hidden", "conference", "creator", "messages_enabled", "can_change_messages_enabled", "min", "title", "stream_dc_id", "record_start_date", "schedule_date", "unmuted_video_count", "invite_link", "send_paid_messages_stars", "default_send_as"]

    ID = 0xefb2b617
    QUALNAME = "types.GroupCall"

    def __init__(self, *, id: int, access_hash: int, participants_count: int, unmuted_video_limit: int, version: int, join_muted: bool | None = None, can_change_join_muted: bool | None = None, join_date_asc: bool | None = None, schedule_start_subscribed: bool | None = None, can_start_video: bool | None = None, record_video_active: bool | None = None, rtmp_stream: bool | None = None, listeners_hidden: bool | None = None, conference: bool | None = None, creator: bool | None = None, messages_enabled: bool | None = None, can_change_messages_enabled: bool | None = None, min: bool | None = None, title: str | None = None, stream_dc_id: int | None = None, record_start_date: int | None = None, schedule_date: int | None = None, unmuted_video_count: int | None = None, invite_link: str | None = None, send_paid_messages_stars: int | None = None, default_send_as: raw.base.Peer | None = None) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.participants_count = participants_count  # int
        self.unmuted_video_limit = unmuted_video_limit  # int
        self.version = version  # int
        self.join_muted = join_muted  # flags.1?true
        self.can_change_join_muted = can_change_join_muted  # flags.2?true
        self.join_date_asc = join_date_asc  # flags.6?true
        self.schedule_start_subscribed = schedule_start_subscribed  # flags.8?true
        self.can_start_video = can_start_video  # flags.9?true
        self.record_video_active = record_video_active  # flags.11?true
        self.rtmp_stream = rtmp_stream  # flags.12?true
        self.listeners_hidden = listeners_hidden  # flags.13?true
        self.conference = conference  # flags.14?true
        self.creator = creator  # flags.15?true
        self.messages_enabled = messages_enabled  # flags.17?true
        self.can_change_messages_enabled = can_change_messages_enabled  # flags.18?true
        self.min = min  # flags.19?true
        self.title = title  # flags.3?string
        self.stream_dc_id = stream_dc_id  # flags.4?int
        self.record_start_date = record_start_date  # flags.5?int
        self.schedule_date = schedule_date  # flags.7?int
        self.unmuted_video_count = unmuted_video_count  # flags.10?int
        self.invite_link = invite_link  # flags.16?string
        self.send_paid_messages_stars = send_paid_messages_stars  # flags.20?long
        self.default_send_as = default_send_as  # flags.21?Peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> GroupCall:
        
        flags = Int.read(b)
        
        join_muted = True if flags & (1 << 1) else False
        can_change_join_muted = True if flags & (1 << 2) else False
        join_date_asc = True if flags & (1 << 6) else False
        schedule_start_subscribed = True if flags & (1 << 8) else False
        can_start_video = True if flags & (1 << 9) else False
        record_video_active = True if flags & (1 << 11) else False
        rtmp_stream = True if flags & (1 << 12) else False
        listeners_hidden = True if flags & (1 << 13) else False
        conference = True if flags & (1 << 14) else False
        creator = True if flags & (1 << 15) else False
        messages_enabled = True if flags & (1 << 17) else False
        can_change_messages_enabled = True if flags & (1 << 18) else False
        min = True if flags & (1 << 19) else False
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        participants_count = Int.read(b)
        
        title = String.read(b) if flags & (1 << 3) else None
        stream_dc_id = Int.read(b) if flags & (1 << 4) else None
        record_start_date = Int.read(b) if flags & (1 << 5) else None
        schedule_date = Int.read(b) if flags & (1 << 7) else None
        unmuted_video_count = Int.read(b) if flags & (1 << 10) else None
        unmuted_video_limit = Int.read(b)
        
        version = Int.read(b)
        
        invite_link = String.read(b) if flags & (1 << 16) else None
        send_paid_messages_stars = Long.read(b) if flags & (1 << 20) else None
        default_send_as = TLObject.read(b) if flags & (1 << 21) else None
        
        return GroupCall(id=id, access_hash=access_hash, participants_count=participants_count, unmuted_video_limit=unmuted_video_limit, version=version, join_muted=join_muted, can_change_join_muted=can_change_join_muted, join_date_asc=join_date_asc, schedule_start_subscribed=schedule_start_subscribed, can_start_video=can_start_video, record_video_active=record_video_active, rtmp_stream=rtmp_stream, listeners_hidden=listeners_hidden, conference=conference, creator=creator, messages_enabled=messages_enabled, can_change_messages_enabled=can_change_messages_enabled, min=min, title=title, stream_dc_id=stream_dc_id, record_start_date=record_start_date, schedule_date=schedule_date, unmuted_video_count=unmuted_video_count, invite_link=invite_link, send_paid_messages_stars=send_paid_messages_stars, default_send_as=default_send_as)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.join_muted else 0
        flags |= (1 << 2) if self.can_change_join_muted else 0
        flags |= (1 << 6) if self.join_date_asc else 0
        flags |= (1 << 8) if self.schedule_start_subscribed else 0
        flags |= (1 << 9) if self.can_start_video else 0
        flags |= (1 << 11) if self.record_video_active else 0
        flags |= (1 << 12) if self.rtmp_stream else 0
        flags |= (1 << 13) if self.listeners_hidden else 0
        flags |= (1 << 14) if self.conference else 0
        flags |= (1 << 15) if self.creator else 0
        flags |= (1 << 17) if self.messages_enabled else 0
        flags |= (1 << 18) if self.can_change_messages_enabled else 0
        flags |= (1 << 19) if self.min else 0
        flags |= (1 << 3) if self.title is not None else 0
        flags |= (1 << 4) if self.stream_dc_id is not None else 0
        flags |= (1 << 5) if self.record_start_date is not None else 0
        flags |= (1 << 7) if self.schedule_date is not None else 0
        flags |= (1 << 10) if self.unmuted_video_count is not None else 0
        flags |= (1 << 16) if self.invite_link is not None else 0
        flags |= (1 << 20) if self.send_paid_messages_stars is not None else 0
        flags |= (1 << 21) if self.default_send_as is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Int(self.participants_count))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.stream_dc_id is not None:
            b.write(Int(self.stream_dc_id))
        
        if self.record_start_date is not None:
            b.write(Int(self.record_start_date))
        
        if self.schedule_date is not None:
            b.write(Int(self.schedule_date))
        
        if self.unmuted_video_count is not None:
            b.write(Int(self.unmuted_video_count))
        
        b.write(Int(self.unmuted_video_limit))
        
        b.write(Int(self.version))
        
        if self.invite_link is not None:
            b.write(String(self.invite_link))
        
        if self.send_paid_messages_stars is not None:
            b.write(Long(self.send_paid_messages_stars))
        
        if self.default_send_as is not None:
            b.write(self.default_send_as.write())
        
        return b.getvalue()
