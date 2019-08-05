# Copyright (C) 2018 Carlos Millett
#
# This file is part of gameTitle.
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.


from os.path import splitext

from .base import UnknownPlatformError
from .gb import GB
from .gbc import GBC
from .gba import GBA
from .nds import NDS
from .n64 import N64
from .ngc import NGC


SYSTEMS = [
    GB,
    GBC,
    GBA,
    NDS,
    N64,
    NGC
]


def match(data):
    for system in SYSTEMS:
        if system.test(data):
            return system()
    raise UnknownPlatformError('ROM not supported')


def read(romFile):
    with open(romFile, 'rb') as rom:
        try:
            gs = match(rom)

        except UnknownPlatformError as err:
            return '{} - {}'.format(romFile, err)

        gs.init(rom)

    return gs.gameTitle
