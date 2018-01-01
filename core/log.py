import logging
import logging.handlers
LOG_FILE = './../file/crawler.log'

handler = logging.handlers.RotatingFileHandler(
    LOG_FILE, maxBytes=4 * 1024 * 1024, backupCount=5)
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)

logger = logging.getLogger('Crawler')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)