# Copyright (C) 2018 Carlos Millett
#
# This file is part of gameTitle.
#
# This software may be modified and distributed under the terms
# of the MIT license.  See the LICENSE file for details.


import argparse

from . import __version__


def setParser():
    parser = argparse.ArgumentParser(prog='gameTitle')
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s v{}'.format(__version__)
    )
    parser.add_argument(
        'path',
        type=str,
        metavar='ROM',
        nargs='+',
        help='ROM file path'
    )

    return parser
