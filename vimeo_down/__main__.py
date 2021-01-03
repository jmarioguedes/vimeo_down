import asyncio

from vimeo_down.const import URL_MASTER
from vimeo_down.downloader import Downloader

#: Recupera o loop de eventos associado à thread principal
from vimeo_down.log import logger

loop = asyncio.get_event_loop()

#: Limpando o diretório de arquivos temporários
pass

#: Agendamento da tarefa principal
main_task = loop.create_task(Downloader(URL_MASTER)(), name='Engine')

#: Execução da tarefa principal
loop.run_until_complete(main_task)

logger.info('Processamento efetuado com sucesso!')


