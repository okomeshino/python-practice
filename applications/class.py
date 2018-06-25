# encoding:utf-8


class TestClass:

    def __init__(self, code, name):
        self.code = code
        self.name = name


classes = [TestClass(1, 'テスト1'), TestClass(2, 'テスト2')]

for test_cls in classes:
    print('============= Class =============')
    print('code --> ' + str(test_cls.code))
    print('name --> ' + test_cls.name)


class Country:

    def __init__(self, country_name):
        self.country_name = country_name


class City(Country):

    def __init__(self, country_name, city_name):
        super().__init__(country_name)
        self.city_name = city_name


classes = [City('Japan', 'Tokyo'), City('USA', 'Washington, D.C.')]

for test_cls in classes:
    print('============= Class =============')
    print('country_name --> ' + test_cls.country_name)
    print('city_name --> ' + test_cls.city_name)


