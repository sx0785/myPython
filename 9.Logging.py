import logging

#create & configure
LOG_FORMAT = "%(levelname)s %(asctime)s -%(message)s"
logging.basicConfig(filename="c:\\src\\MyPython\\mylogging.txt",level=logging.DEBUG,format=LOG_FORMAT)
logger = logging.getLogger()
'''
Level       Numeric value
CRITICAL    50
ERROR       40
WARNING     30
INFO        20
DEBUG       10
NOTSET      0
'''
logger.error("This is my first error")
print(logger.level)
