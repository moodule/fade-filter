# -*- coding: utf-8 -*-

"""
======
FILTER
======

Console script.
"""

from __future__ import absolute_import, division, print_function

from glob import glob
from random import randrange
from typing import List, Tuple, Union

from PIL import Image as img
from PIL.Image import Image

#####################################################################
# SCALE
#####################################################################

def scale_wrapping_image(
        w1: int,
        h1: int,
        ratio: float=1.5) -> Tuple[int, int]:
    """
    Scale an image so that it wraps around the input image size.
    Also square the wrapper image.

    Parameters
    ----------

    Returns
    -------
    out: None.
    """
    return (
        int(max(1., ratio) * max(w1, h1)),
        int(max(1., ratio) * max(w1, h1)))

#####################################################################
# POSITION
#####################################################################

def position_randomly_inside(
        w1: int,
        h1: int,
        w2: int,
        h2: int) -> Union[None, Tuple[int, int]]:
    """
    Position an image randomly, while remaining entirely inside a
    container image.

    Parameters
    ----------

    Returns
    -------
    out: None.
    """
    if (w2 >= w1) and (h2 >= h1):
        return (
            randrange(0, 1 + w2 - w1),  # 0 if w2 == w1
            randrange(0, 1 + h2 - h1))  # same
    else:
        return None

def move_around(
        x: int,
        y: int,
        w1: int,
        h1: int,
        w2: int,
        h2: int,
        limit: int=10) -> Union[None, Tuple[int, int]]:
    """
    Slightly move the smaller image around its position, inside
    the larger image.

    Actually the composition of 4 unidirectional movements, in
    each margin space before and after the smaller image.

    Parameters
    ----------

    Returns
    -------
    out: None.
    """
    if (w2 >= x + w1) and (h2 >= y + h1):
        x_before = randrange(0, 1 + min(limit, x))
        x_after = randrange(0, 1 + min(limit, w2 - w1 - x))
        y_before = randrange(0, 1 + min(limit, y))
        y_after = randrange(0, 1 + min(limit, h2 - h1 - y))
        return (
            x_after - x_before,
            y_after - y_before)
    else:
        return None

#####################################################################
# NOISE
#####################################################################

# so far, randomly spreading the texture does the job
# could be combined with random flip & rotation

#####################################################################
# LAYERS BLENDING
#####################################################################

#####################################################################
# FULL TRANSITION
#####################################################################

#####################################################################
# INPUT
#####################################################################

#####################################################################
# OUTPUT
#####################################################################

def merge_into_an_animation(
        images: List[Image],
        path: str="./out.gif") -> None:
    """
    Merge a list of images into a gif.

    Parameters
    ----------
    images: List.
        A list of image objects, one for each frame.
    path: str.
        The location of the output gif.

    Returns
    -------
    out: None.
    """
    __first, __rest = images[:1], images[1:]
    if __first and __rest:
        __first[0].save(
            fp=path,
            format='GIF',
            append_images=__rest,
            save_all=True,
            duration=40,
            loop=0)


#####################################################################
# MAIN
#####################################################################

if __name__ == "__main__":
    images = [img.open(__f) for __f in glob('/home/flatline/images/erotiques/random/*.jpg')[:10]]
    merge_into_an_animation(images, '/home/flatline/test.gif')
