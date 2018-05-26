# Copyright (C) 2018 Carlos Millett
#
# This file is part of romRenamer.
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.


from .base import Platform


class GBC(Platform):
    def __init__(self):
        super().__init__(
            offset = 0x100,
            size = 80
        )
        self.__header = None
        self.__title = None
        self.__code = None

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
            end = 0x3F
            title = self.__header[start:end]
            self.__title = title.decode().strip('\x00')
        return self.__title

    @property
    def code(self):
        if not self.__code:
            start = 0x3F
            end = 0x43
            code = self.__header[start:end]
            self.__code = code.decode().strip('\x00')
        return self.__code
