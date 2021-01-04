from os import path
from logging import StreamHandler, Formatter, getLogger, DEBUG
from logging.handlers import RotatingFileHandler

#: Definindo o mecanismo de log
output_file = path.join(path.dirname(path.realpath(__file__)), '..', 'logs', 'sms_sender.log')

logger = getLogger('vimeo_down')

formatter = Formatter('| %(levelname)s | %(name)s | %(asctime)s | %(message)s', datefmt='%d/%m/%y %H:%M:%S')

to_console = StreamHandler()
to_file = RotatingFileHandler(output_file, maxBytes=1045 * 1045, backupCount=5, encoding='utf8')

to_console.setFormatter(formatter)
to_file.setFormatter(formatter)

logger.addHandler(to_console)
logger.addHandler(to_file)

logger.setLevel(DEBUG)
