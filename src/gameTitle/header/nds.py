# Copyright (C) 2018 Carlos Millett
#
# This file is part of gameTitle.
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.


from sys import byteorder

from .base import memLocation, Platform


class NDS(Platform):
    def __init__(self):
        header = memLocation(0x00, None, 512)
        title = memLocation(0x00, 0x0C, None)
        code = memLocation(0x0C, 0x10, None)
        super().__init__(header, title, code)
        self.__banner = memLocation(0x68, 0x6C, None)
        self.__titleExtended = memLocation(0x340, 0x440, 256)

    def readBanner(self, data):
        header, *_  = self.readHeader(data)
        bannerSegment = int.from_bytes(
            header[self.__banner.start:self.__banner.end],
            byteorder=byteorder
        )

        data.seek(bannerSegment + self.__titleExtended.start)
        block = data.read(self.__titleExtended.size)
        bTitle = block.decode('utf-16').strip('\x00')
        title = bTitle.split('\n')
        title.pop()

        return ' - '.join(title)

