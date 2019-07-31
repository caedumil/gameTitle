# Copyright (C) 2018 Carlos Millett
#
# This file is part of romRenamer.
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.


from .base import memLocation, Platform


class NGC(Platform):
    def __init__(self):
        header = memLocation(0x0000, None, 1087)
        title = memLocation(0x0020, 0x03FF, None)
        code = memLocation(0x0000, 0x0003, None)
        super().__init__(header, title, code)
