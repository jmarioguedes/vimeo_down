import asyncio

from vimeo_down.const import URL_MASTER
from vimeo_down.downloader import Downloader

#: Recupera o loop de eventos associado à thread principal
from vimeo_down.final import paste_pieces
from vimeo_down.log import logger

loop = asyncio.get_event_loop()

#: Limpando o diretório de arquivos temporários
pass

#: Agendamento da tarefa principal
main_task = loop.create_task(Downloader(URL_MASTER)(), name='Engine')

#: Execução da tarefa principal
loop.run_until_complete(main_task)

#: Gerando o arquivo final de video
paste_pieces('video')
paste_pieces('audio')

logger.info('Processamento efetuado com sucesso!')
