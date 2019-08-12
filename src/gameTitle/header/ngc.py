# Copyright (C) 2018, 2019 Carlos Millett
#
# This file is part of gameTitle.
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.


from .base import memLocation, Platform


class NGC(Platform):
    """
    Nintendo GameCube class.
    """
    def __init__(self):
        header = memLocation(0x0000, None, 1087)
        title = memLocation(0x0020, 0x03FF, None)
        code = memLocation(0x0000, 0x0003, None)
        super().__init__(header, title, code)

    @staticmethod
    def test(data: 'file obj') -> 'bool':
        """
        Check ROM header for the DVD Magic Word at address 0x01C.

        :param data: ROM file obj.
        :returns: True if NGC game ROM.
        """
        magicWord = 'C2 33 9F 3D'
        wordOffset = memLocation(0x001C, 0x001F, 4)

        data.seek(wordOffset.start)
        block = data.read(wordOffset.size)
        dvdMagicWord = bytes.fromhex(magicWord)
        return dvdMagicWord.find(block) == 0
