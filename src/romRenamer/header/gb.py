# Copyright (C) 2018 Carlos Millett
#
# This file is part of romRenamer.
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.


class GB():
    def __init__(self):
        self.__headerOffset = 0x100
        self.__headerSize = 80
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
            start = 0x34
            end = 0x43
            title = self.__header[start:end]
            self.__title = title.decode().strip('\x00')
        return self.__title

    @property
    def code(self):
        return self.__code
