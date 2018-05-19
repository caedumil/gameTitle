# Copyright (C) 2018 Carlos Millett
#
# This file is part of romRenamer.
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.


from sys import byteorder


class NDS():
    def __init__(self):
        self.__headerOffset = 0x00
        self.__headerSize = 512
        self.__header = None
        self.__title = None
        self.__code = None
        self.__bannerOffset = None
        self.__bannerTitleOffset = 0x340
        self.__bannerTitleSize = 256
        self.__bannerTitle = None

    @property
    def headerOffset(self):
        return self.__headerOffset

    @property
    def headerSize(self):
        return self.__headerSize

    @property
    def header(self):
        return self.__header

    @header.setter
    def header(self, header):
        self.__header = header

    @property
    def title(self):
        if not self.__title:
            size = 0x0C
            start = 0x00
            end = start + size
            title = self.__header[start:end]
            self.__title = title.decode().strip('\x00')
        return self.__title

    @property
    def code(self):
        if not self.__code:
            size = 0x04
            start = 0x0C
            end = start + size
            code = self.__header[start:end]
            self.__code = code.decode().strip('\x00')
        return self.__code

    @property
    def bannerOffset(self):
        if not self.__bannerOffset:
            size = 0x04
            start = 0x68
            end = start + size
            offset = self.__header[start:end]
            self.__bannerOffset = int.from_bytes(offset, byteorder=byteorder)
        return self.__bannerOffset

    @property
    def bannerTitleOffset(self):
        return self.__bannerTitleOffset

    @property
    def bannerTitleSize(self):
        return self.__bannerTitleSize

    @property
    def bannerTitle(self):
        return self.__bannerTitle

    @bannerTitle.setter
    def bannerTitle(self, title):
        bTitle = title.decode('utf-16').strip('\x00')
        title, subTitle, _ = bTitle.split('\n')
        self.__bannerTitle = '{} - {}'.format(title, subTitle)
