from page_controller import routes, page_404
from front_controller import fronts
from jinja2 import Template
import os
from models import MainClass
from logger_mod  import Logger, Traceback

logger = Logger('main')
trace = Traceback('MSG')

class Application():

    def __init__(self, route, fronts):
        self.routes = route
        self.fronts = fronts
        self.mainclass = MainClass()

    def __call__(self, environ, start_resp):
        path = environ['PATH_INFO']
        request_method = environ['REQUEST_METHOD']
        if request_method == 'GET':
            logger.log('Get request')
            view = page_404
            if path in self.routes:
                view = self.routes[path]
            request = {}
            for fronts in self.fronts:
                fronts(request)
            request['method'] = request_method
            code, body = view(request)
            start_resp(code, [('Content-Type', 'text/html')])
            return [body.encode('utf-8')]

        elif request_method == 'POST':
            logger.log('POST request')
            trace.log_('msg for Traceback')
            print('POST_METHOD')
            data = self.get_wsgi_input_data(environ)
            data = self.parse_wsgi_input_data(data)
            if path in self.routes:
                view = self.routes[path]
            request = {}
            for fronts in self.fronts:
                fronts(request)
            request['method'] = request_method
            request['applic'] = self.mainclass
            request['data'] = data
            # print(f'REQUEST - {request}')
            code, body = view(request)
            start_resp(code, [('Content-Type', 'text/html')])
            return [body.encode('utf-8')]

    def parse_input_data(self, data: str):
        result = {}
        if data:
            print(data)
            params = data.split('&')
            print(params)
            for item in params:
                if item != '':
                    k, v = item.split('=')
                    result[k] = v
        return result
    def get_wsgi_input_data(self, environ):
        content_length_data = environ.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        data = environ['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data

    def parse_wsgi_input_data(self, data: bytes):
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            print('DATA STRING ', data_str)
            result = self.parse_input_data(data_str)
        return result


application = Application(routes, fronts)

# uwsgi --http :8000 --wsgi-file main.py
