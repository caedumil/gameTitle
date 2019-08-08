# Copyright (C) 2018 Carlos Millett
#
# This file is part of gameTitle.
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.


import os
from sys import exit

from . import cli
from . import header


def main():
    exitCode = 0
    parser = cli.setParser()
    args = parser.parse_args()

    romsList = []
    for path in [os.path.abspath(x) for x in args.path if os.path.exists(x)]:
        if os.path.isdir(path):
            tmp = map((lambda x: os.path.join(path, x)), os.listdir(path))
        else:
            tmp = [path]
        romsList.extend(tmp)

    for rom in romsList:
        try:
            title = header.read(rom)

        except OSError as err:
            exitCode = 1
            title = err.strerror

        finally:
            print(title)

    return exitCode


if __name__ == '__main__':
    exit(main())
