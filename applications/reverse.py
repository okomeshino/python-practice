# encoding:utf-8
python_list = []
python_list.append('python')
python_list.append('izm')
python_list.append('sample')
python_list.append('list')
python_list.append('reversed')

print('--------------------------------')
print('【そのまま表示】')
for value in python_list:
    print(value)

# 逆順にソートして詰め直し
# python_list.reverse()
# print('--------------------------------')
# print('【逆順表示】')
# for value in python_list:
#     print(value)

# スライスで逆順に取得(元リストに影響は与えない)
print('--------------------------------')
print('【逆順表示】')
for value in python_list[::-1]:
    print(value)
