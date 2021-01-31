# -*- coding: utf-8 -*-

"""
===
CLI
===

Console script.
"""

from __future__ import absolute_import, division, print_function

import argparse

#####################################################################
# CLI
#####################################################################

def main():
    """
    The CLI.

    Parameters
    ----------

    Returns
    -------
    out: None.
    """
    parser = argparse.ArgumentParser(
        description='An image filter that slowly eats the content away.')
    parser.add_argument(
        '-t',
        '--texture',
        help='The texture file, which will eventually replace the content',
        required=True)

    args = parser.parse_args()

if __name__ == "__main__":
    main()
