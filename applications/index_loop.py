# encoding:utf-8
test_list = ['python', '-', 'izm', '.', 'com']

for idx, val in enumerate(test_list):
    print(idx, val)

print('------------------------------------')

# 別の開始値で取得
for idx, val in enumerate(test_list, 1):
    print(idx, val)
