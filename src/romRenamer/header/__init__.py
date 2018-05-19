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


extMapping = {
    '.gb': GB,
    '.gbc': GBC,
    '.gba': GBA,
    '.nds': NDS
}

def readHeader(romFile):
    _, ext = splitext(romFile)
    with open(romFile, 'rb') as rom:
        gameSystem = extMapping.get(ext)
        if not gameSystem:
            return None

        gs = gameSystem()
        rom.seek(gs.headerOffset)
        gs.header = rom.read(gs.headerSize)

        if isinstance(gs, NDS):
            rom.seek(gs.bannerOffset + gs.bannerTitleOffset)
            gs.bannerTitle = rom.read(gs.bannerTitleSize)

    return gs
