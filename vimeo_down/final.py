"""Rotinas para juntar os frames em um arquivo MP4"""

__all__ = ['paste_pieces']

from typing import Literal
from os import walk, remove

from vimeo_down.const import DIR_TEMP
from vimeo_down.log import logger


def paste_pieces(tp: Literal['video', 'audio']):
    """Junta os segmentos baixados em um únicos arquivo"""

    final_files = list()
    for root, dirs, files in walk(DIR_TEMP):
        for each in files:
            if each.startswith(tp):
                final_files.append(each)

    file_destiny = f'{DIR_TEMP}\\@{tp}.mp4'
    with open(file_destiny, 'wb') as ipt:
        for each in final_files:
            file_source = f'{DIR_TEMP}\\{each}'
            with open(file_source, 'rb') as otp:
                ipt.write(otp.read())
            remove(file_source)

    logger.info(f'Arquivo gerado com sucesso: {file_destiny}')
