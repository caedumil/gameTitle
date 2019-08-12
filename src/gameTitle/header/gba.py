# Copyright (C) 2018 Carlos Millett
#
# This file is part of gameTitle.
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.


from .base import memLocation, Platform


class GBA(Platform):
    """
    Gameboy Advance class.
    """
    def __init__(self):
        header = memLocation(0x00, None, 192)
        title = memLocation(0xA0, 0xAC, None)
        code = memLocation(0xAC, 0xB0, None)
        super().__init__(header, title, code)

    @staticmethod
    def test(data: 'file obj') -> 'bool':
        """
        Check ROM header for the logo at address 0x004.

        :param data: ROM file obj.
        :returns: True if GBA game ROM.
        """
        logo = (
            '24 FF AE 51 69 9A A2 21 3D 84 82 0A '
            '84 E4 09 AD 11 24 8B 98 C0 81 7F 21'
        )
        logoOffset = memLocation(0x004, 0x0A0, 156)

        data.seek(logoOffset.start)
        block = data.read(logoOffset.size)
        logo = bytes.fromhex(logo)
        return block.find(logo) == 0
