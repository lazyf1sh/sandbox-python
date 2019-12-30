import logging.config

logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')


def run():
    logger2 = logging.getLogger(__name__)
    logger2.debug('debug message')
    logger2.info('info message')
    logger2.warning('warn message')
    logger2.error('error message')
    logger2.critical('critical message')


run()
