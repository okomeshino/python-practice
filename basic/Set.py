# coding:utf-8

test_set_1 = {'python', '-', 'izm', '.', 'com'}
print(test_set_1)

print('---------------------------------------')

for i in test_set_1:
    print(i)

# これはディクショナリ
test_dic = {}

# これはセット
test_set = {'python'}

# からのセットは「set」を使用する
empty_set = set()

test_set_1.remove('-')
test_set_1.discard('.')

print(test_set_1)

