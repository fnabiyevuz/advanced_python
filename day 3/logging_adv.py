"""
import logging

logging.basicConfig(level=logging.INFO,
                    filemode="a+",
                    filename="output.log",
                    format="%(asctime)s [%(levelname)s] %(message)s",
                    )

logging.debug("This is a debug-level log message")  # 10
logging.info("This is an info-level log message")  # 20
logging.warning("This is a warning-level message")
logging.error("This is an error-level message")
logging.critical("This is a critical-level message")

import logging

logger = logging.getLogger(__name__)

# create a file handler
steam_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

steam_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(steam_handler)
logger.addHandler(file_handler)

logger.warning('This is a warning')
logger.info('This is an info')
logger.debug('This is a debug')
"""
import logging.handlers

# create logger
logger = logging.getLogger('simpleExample')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.handlers.RotatingFileHandler('spam.log', maxBytes=2000, backupCount=100)
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# set the formatter for the handler
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')