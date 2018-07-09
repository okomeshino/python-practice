# encoding:utf-8
class AttrTest:

    def __init__(self):
        self.code = -1


# hasattr
attr_test = AttrTest()
attr_test.name = 'python-izm'

print(hasattr(attr_test, 'code'))
print(hasattr(attr_test, 'name'))
print(hasattr(attr_test, 'kana'))

print('-------------------------------')

# getattr
attr_test = AttrTest()
attr_test.name = 'python-izm'

print(getattr(attr_test, 'code'))
print(getattr(attr_test, 'name'))
# print(getattr(attr_test, 'kana')) こちらはエラーになる
print(getattr(attr_test, 'kana', 'No Attr'))
