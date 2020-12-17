import os
from jinja2 import Template
from render_func import render
from logger_mod import Logger

logger = Logger(__name__)


def index_page(request):
    # print('INDEX_PAGE')
    # return '200 OK', [b'INDEX PAGE LOAD']
    logger.log('index page request')
    secret = request.get('secret', None)
    return '200 OK', render('index.html', secret=secret)


def first_page(request):
    secret = request.get('secret', None)
    return '200 OK', render('first.html', secret=secret)


def second_page(request):
    secret = request.get('secret', None)
    return '200 OK', render('second.html', secret=secret)


def page_404(request):
    secret = request.get('secret', None)
    return '404 WHAT', render('404.html', secret=secret)


def contact(request):
    return '200 OK', render('_contact.html')

def category(request):
    # print(f'DEF CATEGORY REQUEST {request.method}')
    if request['method'] == 'GET':
        return '200 OK', render('category.html')
    elif request['method'] == 'POST':
        pass

def course_create(request):
    if request['method'] == 'GET':
        return '200 OK', render('course_create.html')
    elif request['method'] == 'POST':
        print('course_create')
        print(request['applic'])
        data = request['data']
        print(data)
        applic = request['applic']
        applic.create_courses(data['title'])
        print(applic.course)
        return '200 OK', render('course_create.html', applic=applic.course)

def category_create(request):
    if request['method']== 'GET':
        return '200 OK', render('category_create.html')
    elif request['method'] == 'POST':
        print('course_create')
        print(request['applic'])
        data = request['data']
        print(data)
        applic = request['applic']
        #def create_category(self, cat_name, form, cours_name=None):
        applic.create_category(cat_name=data['title'], form='online')
        print(applic.category)
        return '200 OK', render('category_create.html',applic=applic.category)


routes = {
    '/': index_page,
    '/first/': first_page,
    '/second/': second_page,
    '/contact/': contact,
    '/category/': category,
    '/course_create/': course_create,
    '/category_create/': category_create,

}
