# -*- coding: utf-8 -*-

"""
======
FILTER
======

Console script.
"""

from __future__ import absolute_import, division, print_function

from glob import glob
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
# NOISE
#####################################################################

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
