# Copyright (C) 2018 Carlos Millett
#
# This file is part of romRenamer.
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.


import os
from sys import exit

from . import cli
from . import header


def main():
    parser = cli.setParser()
    args = parser.parse_args()

    romsList = []
    for path in [os.path.abspath(x) for x in args.path if os.path.exists(x)]:
        if os.path.isdir(path):
            tmp = map((lambda x: os.path.join(path, x)), os.listdir(path))
        else:
            tmp = [path]
        romsList.extend(tmp)

    romsInfo = [header.readHeader(x) for x in romsList]

    for i in [x for x in romsInfo if x]:
        print(i.title)

    return 0


if __name__ == '__main__':
    exit(main())
