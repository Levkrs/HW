import logging
import logging.handlers
import time
import os



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
        LOGGER = logging.getLogger('server')
        LOGGER.addHandler(LOG_FILE)
        LOGGER.setLevel(logging.DEBUG)
        text = text + ' ' + str(time.time())
        LOGGER.debug(text)
if __name__ == '__main__':
    x = Logger('test')
    x.log('TEST LOG')

