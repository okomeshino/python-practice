# encoding:utf-8

import datetime


class TestClass:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # クラスメソッド
    @classmethod
    def sample_class_method(cls, date_diff=0):
        today = datetime.date.today()
        d = today + datetime.timedelta(date_diff)
        return cls(d.year, d.month, d.day)


# インスタンス化しないで呼び出し
test_class_1 = TestClass.sample_class_method()
print(test_class_1.year, test_class_1.month, test_class_1.day)

# インスタンス化しないで呼び出し
test_class_2 = TestClass.sample_class_method(-10)
print(test_class_2.year, test_class_2.month, test_class_2.day)

# 通常のインスタンス
test_class_3 = TestClass(2000, 1, 1)
print(test_class_3.year, test_class_3.month, test_class_3.day)
