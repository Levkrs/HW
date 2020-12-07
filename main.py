from page_controller import routes, page_404
from front_controller import fronts
from jinja2 import Template
import os
class Application():

    def __init__(self, route, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_resp):
        # print('WORK')
        # print(environ)
        path = environ['PATH_INFO']
        print(path)
        print(f'slef.routes : {self.routes}')
        view = page_404
        if path in self.routes:
            print('if path')
            view = self.routes[path]
            # view = '200 OK', render('index.html', object_list=[{'name': 'Leo'}, {'name': 'Kate'}])
            # print(view)
        request = {}
        for fronts in self.fronts:
            fronts(request)
        code, body = view(request)

        start_resp(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]


def render(template_name, folder='templates', **kwargs):
    file_path = os.path.join(folder, template_name)
    # Открываем шаблон по имени
    with open(file_path, encoding='utf-8') as f:
        # Читаем
        template = Template(f.read())
    # рендерим шаблон с параметрами
    return template.render(**kwargs)


application = Application(routes, fronts)
