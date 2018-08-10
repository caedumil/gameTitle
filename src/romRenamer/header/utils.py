# Copyright (C) 2018 Carlos Millett
#
# This file is part of romRenamer.
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.


from os.path import splitext

from .gb import GB
from .gbc import GBC
from .gba import GBA
from .nds import NDS


extensionMapping = {
    '.gb': GB,
    '.gbc': GBC,
    '.gba': GBA,
    '.nds': NDS
}


def read(romFile):
    _, ext = splitext(romFile)
    gameSystem = extensionMapping.get(ext)
    if not gameSystem:
        return None

    with open(romFile, 'rb') as rom:
        gs = gameSystem()
        headerInfo = gs.readHeader(rom)

        if isinstance(gs, NDS):
            extendedInfo = gs.readBanner(rom)
            return extendedInfo

    return headerInfo.title
