import logging
import logging.handlers
import time
import os
import traceback


class Logger():
    def __init__(self, name):
        self.name = name

    def log(self, text):
        PATH = os.path.dirname(os.path.abspath(__file__))
        PATH = os.path.join(PATH, 'logger_files/')
        PATH = os.path.join(PATH, self.name)
        print(PATH)
        # print('log--->', text)
        LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf8', interval=1, when='D')
        LOGGER = logging.getLogger(self.name)
        LOGGER.addHandler(LOG_FILE)
        LOGGER.setLevel(logging.DEBUG)
        text = text + ' ' + str(time.time())
        LOGGER.debug(text)


class Traceback():
    def __init__(self, msg):
        self.msg = msg

    def log_(self, text):
        print(f'---------{text}')
        print(f'TRACEBACK - {traceback.format_stack()}')


if __name__ == '__main__':
    x = Logger('test')
    x.log('TEST LOG')
    y = Traceback('msg')
    y.log_('test. msg')
