# coding:utf-8

import testmod
from testmod import TestClass

test_class_1 = testmod.TestClass()
test_class_1.test_method('1')

test_class_2 = TestClass()
test_class_2.test_method('2')

# 別名でインポートする場合(as)
from datetime import datetime
print(datetime.today())

from datetime import datetime as d
print(d.today())

