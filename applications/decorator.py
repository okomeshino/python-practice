# encoding:utf-8
from contextlib import contextmanager


@contextmanager
def context_manager_test():
    print('enter')
    # asで渡されるオブジェクトを指定
    yield 'as_obj'
    print('exit')


with context_manager_test() as as_obj:
    print('with')
    print(as_obj)
