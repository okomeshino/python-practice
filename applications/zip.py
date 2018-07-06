# encoding:utf-8
from itertools import zip_longest

item_list = ['desktop', 'laptop', 'tablet', 'smartphone']
stock_list = [12, 83, 55, 0]

for item_name, stock_count in zip(item_list, stock_list):
    print('{} / {}'.format(item_name, stock_count))

print('----------------------------------------')

# 要素数が一致していない場合は少ない方に合わせる
stock_list = [12, 83, 55]

for item_name, stock_count in zip(item_list, stock_list):
    print('{} / {}'.format(item_name, stock_count))

print('----------------------------------------')

# zip_longest()の場合は多い方に合わせる（fillvalueの指定が無い場合はNone）
for item_name, stock_count in zip_longest(item_list, stock_list):
    print('{} / {}'.format(item_name, stock_count))

# zip_longest()の場合は多い方に合わせる（fillvalueの指定あり）
for item_name, stock_count in zip_longest(item_list, stock_list, fillvalue='no stock'):
    print('{} / {}'.format(item_name, stock_count))
