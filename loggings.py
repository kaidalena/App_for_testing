import logging
from logging.handlers import TimedRotatingFileHandler

def create_log(name = 'test'):
    name_log_file = 'logs/{}.log'.format(name)

    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)

    handler = TimedRotatingFileHandler(name_log_file, when='D', interval=1, backupCount=5)
    handler.setLevel(logging.DEBUG)

    format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(format)

    log.addHandler(handler)

    return log


loggers = {
    'app': create_log('app'),
    'migration': create_log('migration'),
    'test': create_log('test'),
    'job': create_log('job')
}


def get_loggers():
    global loggers
    return loggers