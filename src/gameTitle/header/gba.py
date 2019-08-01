# Copyright (C) 2018 Carlos Millett
#
# This file is part of gameTitle.
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.


from .base import memLocation, Platform


class GBA(Platform):
    def __init__(self):
        header = memLocation(0x00, None, 192)
        title = memLocation(0xA0, 0xAC, None)
        code = memLocation(0xAC, 0xB0, None)
        super().__init__(header, title, code)
