import os
from jinja2 import Template
from render_func import render


def index_page(request):
    # print('INDEX_PAGE')
    # return '200 OK', [b'INDEX PAGE LOAD']
    secret = request.get('secret', None)
    return '200 OK', render('index.html', secret=secret)


def first_page(request):
    secret = request.get('secret', None)
    return '200 OK', render('first.html', secret=secret)


def second_page(request):
    secret = request.get('secret', None)
    return '200 OK', render('second.html', secret=secret)


def page_404(request):
    # print('PAGE_404')
    secret = request.get('secret', None)
    return '404 WHAT', render('404.html', secret=secret)

def contact(request):
    return '200 OK', render('_contact.html')


routes = {
    '/': index_page,
    '/first/': first_page,
    '/second/': second_page,
    '/contact/': contact,

}


# def render(template_name, folder='templates', **kwargs):
#     file_path = os.path.join(folder, template_name)
#     # Открываем шаблон по имени
#     with open(file_path, encoding='utf-8') as f:
#         # Читаем
#         template = Template(f.read())
#     # рендерим шаблон с параметрами
#     return template.render(**kwargs)
