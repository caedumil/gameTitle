# Copyright (C) 2018, 2019 Carlos Millett
#
# This file is part of gameTitle.
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.


from .base import memLocation, Platform


class N64(Platform):
    """
    Nintendo 64 class.
    """
    def __init__(self):
        header = memLocation(0x00, None, 4096)
        title = memLocation(0x20, 0x34, None)
        code = memLocation(None, None, None)
        super().__init__(header, title, code)

    @staticmethod
    def test(data: 'file obj') -> 'bool':
        """
        Check ROM header first 4 bytes for a specific value.

        :param data: ROM file obj.
        :returns: True if N64 game ROM.
        """
        value = '80 37 12 40'
        offset = memLocation(0x00, 0x03, 4)

        data.seek(offset.start)
        block = data.read(offset.size)
        value = bytes.fromhex(value)
        return value.find(block) == 0
