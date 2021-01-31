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
        'input',
        type=str,
        help='The path to the input image, which is the starting point of the video',
        required=True)
    parser.add_argument(
        'texture',
        type=str,
        help='The texture file, which will eventually replace the content',
        required=True)
    parser.add_argument(
        '-b',
        '--blend',
        type=str,
        default='difference',
        help='The mode to use when blending layers',
        required=False)
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        default='gif',
        help='The format of the output: jpg / gif',
        required=False)
    parser.add_argument(
        '-i',
        '--iterations',
        type=int,
        default=10,
        help='The number of times the effect is applied',
        required=False)
    parser.add_argument(
        '-n',
        '--noise',
        type=int,
        default=0,
        help='The level of random noise, at each step',
        required=False)
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        help='The path to the output image / gif',
        required=False)
    parser.add_argument(
        '-p',
        '--postprocessing',
        type=int,
        default=0,
        help='Level for the sharpening filter',
        required=False)
    parser.add_argument(
        '-w',
        '--width',
        type=int,
        default=0,
        help='The width of the output\'s frame, 0 to keep the input\'s width',
        required=False)
    args = parser.parse_args()

if __name__ == "__main__":
    main()
