import logging
import os


""" OLD STUFF


LOGDIR = os.path.join(BASEDIR, 'log', 'autoinstall.log')

logging.basicConfig(filename=LOGDIR,
                    level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)10s: %(message)s')

LOGGER = logging
"""

BASEDIR = os.path.abspath(os.path.dirname(__file__))
LOGDIR = os.path.join(BASEDIR, 'log', 'autoinstall.log')
# create logger
logger = logging.getLogger("autoinstall_log")
logger.setLevel(logging.INFO)
logger.basicConfig(filename=LOGDIR)
# create console handler and set level to debug
ch = logging.StreamHandler()
#LEVELS: DEBUG - INFO - WARNING - ERROR - CRITICAL
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("[%(asctime)s] [%(levelname)10s] Message: %(message)s")
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)

LOGGER = logger
