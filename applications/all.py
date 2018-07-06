# encoding:utf-8
test_list_1 = [0, 100, 300, 800, 150, 0, 30]
test_list_2 = [[],[],[]]
test_list_3 = [['python', 'izm', 'com'], ['www'], ['http']]

# all,すべての要素が真の場合にTrueを返す
print(all(test_list_1))
print(all(test_list_2))
print(all(test_list_3))

print('---------------------------------')

# any,いずれかの要素が真の場合にTrueを返す
print(any(test_list_1))
print(any(test_list_2))
print(any(test_list_3))
