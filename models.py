import abc

from logger_mod import Logger

logger = Logger(__name__)


class Courses:
    def __init__(self, name):
        self.name = name
        self.category = []


class Category:
    def __init__(self, name, type_, course=None):
        self.name = name
        self.type = type_
        self.course = course
        print('----')


class MainClass:
    def __init__(self):
        self.course = {}
        self.category = []

    def create_courses(self, name_course):
        cours = Courses(name_course)
        if self.course.get(cours.name):
            param = self.course[cours.name]
            param.append(cours)
        else:
            self.course[cours.name] = [cours]
        logger.log('CREATE COURSES')

    def create_category(self, cat_name, form, cours_name=None):
        # if self.course.get(cours_name):
        cours = cours_name
        cat = Category(cat_name, form, cours)
        self.category.append(cat)

        logger.log('CREATE CATEGORY')
        # else:
        #     print('Error - Нет такого курса')

    def get_categorys(self):
        return self.category


if __name__ == '__main__':
    maincls = MainClass()
    maincls.create_courses('Snowboard')
    print(maincls.course)
    maincls.create_courses('Snowboard')
    maincls.create_category('Пересеченка', 'online', 'Snowboard')
    maincls.create_category('Прямая', 'online', 'Snowboard')
    print(maincls.course)
    print(maincls.category)
