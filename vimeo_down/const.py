"""Constantes globais do projeto"""

from os import path
from configparser import ConfigParser

from vimeo_down.log import logger

config_file_name = path.join(path.dirname(path.realpath(__file__)), 'config.ini')

cfg = ConfigParser()
cfg.read(config_file_name)

URL_MASTER = cfg.get('GENERAL', 'URL_MASTER', raw=True)
DIR_TEMP = cfg.get('GENERAL', 'DIR_TEMP')

logger.info(f'Diretório de trabalho: {DIR_TEMP}')
logger.info(f'URL do documento mestre: {URL_MASTER}')
