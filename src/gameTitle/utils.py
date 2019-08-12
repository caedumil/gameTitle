# Copyright (C) 2018 Carlos Millett
#
# This file is part of gameTitle.
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.


from . import header


SYSTEMS = [
    header.GB,
    header.GBC,
    header.GBA,
    header.NDS,
    header.N64,
    header.NGC
]


def match(data: 'file obj') -> 'ROM obj':
    """
    Match given file to a ROM type.

    :param data: ROM file object.
    :returns: specific ROM class object.
    :raises UnknownPlatformError: matching failed.
    """
    for system in SYSTEMS:
        if system.test(data):
            return system()
    raise header.UnknownPlatformError('ROM not supported')


def read(romFile: 'str') -> 'str':
    """
    Open ROM file to read the title from the header.

    :param romFile: ROM file path.
    :returns: title
    """
    with open(romFile, 'rb') as rom:
        try:
            gs = match(rom)

        except header.UnknownPlatformError as err:
            return '{} - {}'.format(romFile, err)

        gs.init(rom)

    return gs.gameTitle
