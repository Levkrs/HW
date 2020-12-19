import time

def debug(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('DEBUG-------->', func.__name__, end - start)
        return result

    return inner


def first_func(func):

    def rty(*args, **kwargs):
        print(f'decor_func res')
        if kwargs['test'] == 5:
            return 'stop'
        res = func(*args, **kwargs)
        print(res)
        # return res

    return rty

# @debug
@first_func
def my_func(x, test=None):
    x = x+1
    print(f'my_func {x}')
    return x

if __name__ == '__main__':
    my_func(3, test=5)