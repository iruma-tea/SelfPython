from datetime import datetime
from time import sleep, time


def time_deco(func):
    def inner(*args, **keywds):
        print(f'{func.__name__} Start {datetime.fromtimestamp(time())}')
        result = func(*args, **keywds)
        print(f'{func.__name__} end {datetime.fromtimestamp(time())}')
        return result
    return inner


@time_deco
def hoge():
    sleep(3)
    print('hoge is running.')


hoge()
