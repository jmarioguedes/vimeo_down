"""Rotinas para juntar os frames em um arquivo MP4"""

__all__ = ['paste_pieces']

from typing import Literal
from os import walk

from vimeo_down.const import DIR_TEMP


def paste_pieces(tp: Literal['video', 'audio']):
    """Juntos os segmentos baixados em um únicos arquivo"""

    final_files = list()
    for root, dirs, files in walk(DIR_TEMP):
        for each in files:
            if each.startswith(tp):
                final_files.append(each)

    with open(f'{DIR_TEMP}\\@{tp}.mp4', 'wb') as ipt:
        for each in final_files:
            with open(f'{DIR_TEMP}\\{each}', 'rb') as otp:
                ipt.write(otp.read())
