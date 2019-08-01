# Copyright (C) 2018 Carlos Millett
#
# This file is part of gameTitle.
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.


from .base import memLocation, Platform


class GBC(Platform):
    def __init__(self):
        header = memLocation(0x100, None, 80)
        title = memLocation(0x34, 0x3F, None)
        code = memLocation(0x3F, 0x43, None)
        super().__init__(header, title, code)
