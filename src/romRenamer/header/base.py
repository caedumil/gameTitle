# Copyright (C) 2018 Carlos Millett
#
# This file is part of romRenamer.
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.


from collections import namedtuple


memLocation = namedtuple('Mem', ['start', 'end', 'size'])
romInfo = namedtuple('ROM', ['header', 'title', 'code'])


class Platform():
    def __init__(self, header, title, code):
        self.__header = header
        self.__title = title
        self.__code = code

    @property
    def header(self):
        return self.__header

    @property
    def title(self):
        return self.__title

    @property
    def code(self):
        return self.__code

    def readHeader(self, data):
        data.seek(self.__header.start)
        header = data.read(self.__header.size)

        bTitle = header[self.__title.start:self.__title.end]
        title = bTitle.decode().strip('\x00')
        if self.__code.start:
            bCode = header[self.__code.start:self.__code.end]
            code = bCode.decode().strip('\x00')
        else:
            code = None

        return romInfo(header, title, code)
