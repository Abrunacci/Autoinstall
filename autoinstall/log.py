import logging
import logging.handlers
import os
import sys
import time


BASEDIR = os.path.abspath(os.path.dirname(__file__))
LOGDIR = os.path.join(BASEDIR, 'log', 'autoinstall.log')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

log_format = "".join(["[%(asctime)s] [%(levelname)8s] Message: ",
                      "%(message)s"])

formatter = logging.Formatter(fmt=log_format)
# Format UTC Time
formatter.converter = time.gmtime

# File Handler Logger
LOGDIR = os.path.join(BASEDIR, 'log')
if not os.path.isdir(LOGDIR):
    os.mkdir(LOGDIR)

LOGFILE = os.path.join(
    LOGDIR,
    'autoinstall_log.log',
    )
fh = logging.handlers.RotatingFileHandler(filename=LOGFILE,
                                          maxBytes=10e6,
                                          backupCount=10)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

# create logger
# create console handler and set level to debug
ch = logging.StreamHandler()
# add formatter to ch
ch.setFormatter(formatter)
ch.setLevel(logging.INFO)
# add ch to logger
logger.addHandler(ch)


LOGGER = logger
