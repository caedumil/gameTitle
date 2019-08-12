# Copyright (C) 2018 Carlos Millett
#
# This file is part of gameTitle.
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.


from .base import memLocation, Platform


class GB(Platform):
    """
    Gameboy class.
    """
    def __init__(self):
        header = memLocation(0x100, None, 80)
        title = memLocation(0x34, 0x43, None)
        code = memLocation(None, None, None)
        super().__init__(header, title, code)

    @staticmethod
    def test(data: 'file obj') -> 'bool':
        """
        Check ROM header for the logo at address 0x104.

        :param data: ROM file obj.
        :returns: True if GB game ROM.
        """
        logo = (
            'CE ED 66 66 CC 0D 00 0B 03 73 00 83 '
            '00 0C 00 0D 00 08 11 1F 88 89 00 0E'
        )
        logoOffset = memLocation(0x104, 0x133, 0x02F)
        data.seek(logoOffset.start)
        block = data.read(logoOffset.size)
        logo = bytes.fromhex(logo)
        isGB = block.find(logo) == 0

        cgbFlag = ['80', 'C0']
        cgbFlagOffset = memLocation(0x143, 0x144, 0x001)
        data.seek(cgbFlagOffset.start)
        cgb = data.read(cgbFlagOffset.size)
        flag = [x for x in map(bytes.fromhex, cgbFlag)]
        return isGB and not cgb in flag
