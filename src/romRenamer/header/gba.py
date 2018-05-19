# Copyright (C) 2018 Carlos Millett
#
# This file is part of romRenamer.
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.


class GBA():
    def __init__(self):
        self.__headerOffset = 0x00
        self.__headerSize = 192
        self.__header = None
        self.__title = None
        self.__code = None

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
            start = 0xA0
            end = start + size
            title = self.__header[start:end]
            self.__title = title.decode().strip('\x00')
        return self.__title

    @property
    def code(self):
        if not self.__code:
            size = 0x04
            start = 0xAC
            end = start + size
            code = self.__header[start:end]
            self.__code = code.decode().strip('\x00')
        return self.__code
