# -*- coding: utf-8 -*-

"""
===
CLI
===

Console script.
"""

from __future__ import absolute_import, division, print_function

import argparse

from PIL import Image as pil

from eataway import eat_image_away, merge_into_an_animation

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

    # define the CLI parameters
    __parser = argparse.ArgumentParser(
        description='An image filter that slowly eats the content away.')
    __parser.add_argument(
        'input',
        type=str,
        help='The path to the input image, which is the starting point of the video')
    __parser.add_argument(
        'texture',
        type=str,
        help='The texture file, which will eventually replace the content')
    __parser.add_argument(
        '-b',
        '--blend',
        type=str,
        default='difference',
        help='The mode to use when blending layers',
        required=False)
    __parser.add_argument(
        '-d',
        '--duration',
        type=int,
        default=100,
        help='The timespan between 2 successive gif frames',
        required=False)
    __parser.add_argument(
        '-f',
        '--format',
        type=str,
        default='gif',
        help='The format of the output: jpg / gif',
        required=False)
    __parser.add_argument(
        '-i',
        '--iterations',
        type=int,
        default=10,
        help='The number of times the effect is applied',
        required=False)
    __parser.add_argument(
        '-n',
        '--noise',
        type=int,
        default=0,
        help='The level of random noise, at each step',
        required=False)
    __parser.add_argument(
        '-o',
        '--output',
        type=str,
        default='./out.gif',
        help='The path to the output image / gif',
        required=False)
    __parser.add_argument(
        '-p',
        '--postprocessing',
        type=int,
        default=0,
        help='Level for the sharpening filter',
        required=False)
    __parser.add_argument(
        '-w',
        '--width',
        type=int,
        default=0,
        help='The width of the output\'s frame, 0 to keep the input\'s width',
        required=False)

    # retrieve and parse the argument values
    __args = __parser.parse_args()
    __max_width = __args.width if __args.width >= 0 else 512

    # initiate
    __frames = []

    with pil.open(__args.input).convert('LA').convert('RGBA') as __input:
        with pil.open(__args.texture).convert('LA').convert('RGBA') as __texture:
            __frames = eat_image_away(
                image=__input,
                texture=__texture,
                iterations=__args.iterations,
                size=(__max_width, __max_width),
                opacity=1.0,
                noise=__args.noise,
                sharpen=False,
                invert=False)

    merge_into_an_animation(
        images=__frames,
        path=__args.output,
        duration=__args.duration)

if __name__ == "__main__":
    main()
