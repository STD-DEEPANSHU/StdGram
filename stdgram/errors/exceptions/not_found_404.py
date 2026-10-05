# StdGram - Telegram MTProto API Client Library for Python
#
# Copyright (C) 2017-present Dan <https://github.com/delivrance>
# Copyright (C) 2024-present KurimuzonAkuma <https://github.com/KurimuzonAkuma>
#
# This file is part of StdGram.
#
# StdGram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# StdGram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with StdGram. If not, see <https://www.gnu.org/licenses/>.

from ..rpc_error import RPCError
from .bad_request_400 import (
    MethodInvalid,
    PeerIdInvalid,
)


class NotFound(RPCError):
    """Not Found"""
    CODE = 404
    """``int``: RPC Error Code"""
    NAME = __doc__


class MethodInvalid404(MethodInvalid, NotFound):
    """The specified method is invalid."""
    ID = "METHOD_INVALID"
    """``str``: RPC Error ID"""
    CODE = 404
    """``int``: RPC Error Code"""
    NAME = "Not Found"
    """``str``: RPC Error Name"""
    MESSAGE = __doc__


class PeerIdInvalid404(PeerIdInvalid, NotFound):
    """The provided peer id is invalid."""
    ID = "PEER_ID_INVALID"
    """``str``: RPC Error ID"""
    CODE = 404
    """``int``: RPC Error Code"""
    NAME = "Not Found"
    """``str``: RPC Error Name"""
    MESSAGE = __doc__


