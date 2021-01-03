"""Efetua o download do documento mestre, disparando as diversas tarefas para download dos frames"""

__all__ = ['Downloader']

import asyncio
from typing import Literal
from urllib.parse import urljoin
from base64 import b64decode

from aiohttp import ClientSession

from vimeo_down.const import DIR_TEMP
from vimeo_down.log import logger


async def file_save(content, tp, sequence):
    file_name = f'{DIR_TEMP}\\{tp}_{sequence:0>10d}'
    with open(file_name, 'wb') as file:
        file.write(content)


class DownFrame:
    """Efetua o download de um frame, de áudio ou vídeo."""

    def __init__(self, *, url: str, tp: Literal['audio', 'video'], sequence: int):
        self.url = url
        self.tp = tp
        self.sequence = sequence

    async def __call__(self) -> bool:
        logger.info(f"Baixando o frame ...{self.url[-50:]}")

        async with ClientSession() as session:
            async with session.get(self.url) as response:
                if response.status != 200:
                    return False

                raw_content = await response.content.read()
                await file_save(raw_content, self.tp, self.sequence)
                return True


class Downloader:
    """Efetua o download do documento mestre."""

    def __init__(self, url_master: str):
        self.url_master = url_master

    async def __call__(self, *args, **kwargs):
        """Processamento principal.

        Efetua o download do documento mestre e em seguida inicia as tarefas de download dos frames
        """
        async with ClientSession() as session:
            async with session.get(self.url_master) as response:
                logger.info(f'Download do documento mestre - Status: {response.status}')
                content = await response.json(encoding='utf-8')

        video_url_base = urljoin(urljoin(self.url_master, content['base_url']), content['video'][0]['base_url'])
        audio_url_base = urljoin(urljoin(self.url_master, content['base_url']), content['audio'][0]['base_url'])

        logger.debug(f'URL base para os vídeos: {video_url_base}')
        logger.debug(f'URL base para os áudios: {audio_url_base}')

        all_tasks = list()

        frame_zero = b64decode(content['video'][0]['init_segment'])
        await file_save(frame_zero, 'video', 0)

        for idx, video in enumerate(content['video'][0]['segments']):
            url = urljoin(video_url_base, video['url'])
            task = DownFrame(url=url, tp='video', sequence=idx + 1)()
            all_tasks.append(task)

        frame_zero = b64decode(content['audio'][0]['init_segment'])
        await file_save(frame_zero, 'audio', 0)

        for idx, audio in enumerate(content['audio'][0]['segments']):
            url = urljoin(audio_url_base, audio['url'])
            task = DownFrame(url=url, tp='audio', sequence=idx + 1)()
            all_tasks.append(task)

        work_load = list()
        while all_tasks:
            qtt = 0
            while all_tasks:
                work_load.append(all_tasks.pop(0))
                qtt += 1
                if qtt > 10:
                    break

            logger.info('Aguardando carga de trabalho ...')
            results = await asyncio.gather(*work_load)
            work_load.clear()

            if not any(results):
                raise Exception('Houve um erro em alguma chamada de frame!')
