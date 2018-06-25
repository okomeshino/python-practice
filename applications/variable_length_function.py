# encoding:utf-8


def test_func_1(*args):
    print(args)


test_func_1(1, 2, 3, 4, 5)


# タプルで渡される
def test_func_2(code, name, *args):
    print(code, name)
    print(args)


test_func_2(100, 'python-izm', 'JP', 'US')


# ディクショナリで渡される
def test_func_3(**kwargs):
    print(kwargs)


test_func_3(code=100, name='python-izm')


def test_func_4(code, name, kana, *args, **kwargs):
    print(code, name, kana)
    print(args)
    print(kwargs)


test_func_4(
    100, 'python-izm', 'パイソンイズム',
    'JP', 'US',
    email='xxxx@xxxx', city='Tokyo'
)

