# encoding:utf-8

for_sample = ["python", "-", "izm", "for", "statement", "sample"]

# リストのループ
for value in for_sample:
    print(value)

# 文字列のループ
for value in 'ABCDEF':
    print(value)

# 複数の値へ分割して取得
test_list_1 = [['https', 'www'], ['python-izm', 'com']]

for value in test_list_1:
    print(value)

for value_1, value_2 in test_list_1:
    print(value_1, value_2)
