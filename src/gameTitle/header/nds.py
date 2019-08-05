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

        self.__bannerOffset = memLocation(0x68, 0x6C, None)
        self.__extendedTitleOffset = memLocation(0x340, 0x440, 256)
        self.__romBanner = None
        self.__gameTitle = None

    def init(self, data):
        super().init(data)
        bannerSegment = int.from_bytes(
            self.romHeader[self.__bannerOffset.start:self.__bannerOffset.end],
            byteorder=byteorder
        )
        data.seek(bannerSegment + self.__extendedTitleOffset.start)
        banner = data.read(self.__extendedTitleOffset.size)
        self.__romBanner = banner

    @property
    def gameTitle(self):
        if not self.__gameTitle:
            bTitle = self.__romBanner.decode('utf-16').strip('\x00')
            title = bTitle.split('\n')
            self.__gameTitle = ' - '.join(title[:-1])
        return self.__gameTitle

    @staticmethod
    def test(data):
        logo = (
            '24 FF AE 51 69 9A A2 21 3D 84 82 0A '
            '84 E4 09 AD 11 24 8B 98 C0 81 7F 21'
        )
        logoOffset = memLocation(0x0C0, 0x15C, 156)

        data.seek(logoOffset.start)
        block = data.read(logoOffset.size)
        logo = bytes.fromhex(logo)
        return block.find(logo) == 0
