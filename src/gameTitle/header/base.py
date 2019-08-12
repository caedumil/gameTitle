# Copyright (C) 2018 Carlos Millett
#
# This file is part of gameTitle.
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.


from collections import namedtuple


memLocation = namedtuple('MemOffset', ['start', 'end', 'size'])


class Platform():
    """
    Base class for ROM type classes.
    """
    def __init__(
        self,
        headerOffset: 'memOffset',
        titleOffset: 'memOffset',
        codeOffset: 'memOffset'
    ):
        self.__headerOffset = headerOffset
        self.__titleOffset = titleOffset
        self.__codeOffset = codeOffset
        self.__romHeader = None
        self.__gameTitle = None
        self.__gameCode = None

    @property
    def romHeader(self):
        return self.__romHeader

    @property
    def gameTitle(self):
        if not self.__gameTitle:
            bTitle = self.__romHeader[self.__titleOffset.start:self.__titleOffset.end]
            self.__gameTitle = bTitle.decode().strip('\x00')
        return self.__gameTitle

    @property
    def gameCode(self):
        if self.__codeOffset.start and not self.__gameCode:
            bCode = self.__romHeader[self.__codeOffset.start:self.__codeOffset.end]
            code = bCode.decode().strip('\x00')
        return self.__gameCode

    def init(self, data: 'file obj'):
        """
        Extract header from file.

        :param data: ROM file obj.
        """
        data.seek(self.__headerOffset.start)
        header = data.read(self.__headerOffset.size)
        self.__romHeader = header

    @staticmethod
    def test(data: 'file obj') -> 'bool':
        """
        Check ROM header for specific data.

        :param data: ROM file obj.
        :returns: whether the header is of the ROM type.
        """
        raise NotImplementedError()


class UnknownPlatformError(Exception):
    """
    Raised when Rom header can't be matched against supported types
    """
