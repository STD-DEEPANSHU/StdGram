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

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import TYPE_CHECKING

from stdgram import raw
from stdgram.raw.core import BaseTypeMeta


if TYPE_CHECKING:
    MessageExtendedMedia = raw.types.MessageExtendedMedia | raw.types.MessageExtendedMediaPreview
else:
    # noinspection PyRedeclaration
    class MessageExtendedMedia(metaclass=BaseTypeMeta):  # type: ignore
        """Telegram API base type.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: stdgram.raw.types

        .. autosummary::
            :nosignatures:

            MessageExtendedMedia
            MessageExtendedMediaPreview
        """

        QUALNAME = "stdgram.raw.base.MessageExtendedMedia"
        __union_types__ = raw.types.MessageExtendedMedia | raw.types.MessageExtendedMediaPreview

        def __init__(self):
            raise TypeError("Base types can only be used for type checking purposes: "
                            "you tried to use a base type instance as argument, "
                            "but you need to instantiate one of its constructors instead. "
                            "More info: https://docs.kurigram.icu/telegram/base/message-extended-media")
