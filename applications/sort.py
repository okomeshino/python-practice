# encoding:utf-8
python_list = []
python_list.append(100)
python_list.append(200)
python_list.append(10)
python_list.append(800)
python_list.append(60)

print('---------------------------------------')
print('【そのまま表示】')
for value in python_list:
    print(value)

# リストをソートして詰め直し
# python_list.sort()
# print('---------------------------------------')
# print('【ソート表示】')
# for value in python_list:
#     print(value)

# リストをソートして詰め直しはしない
print('---------------------------------------')
print('【ソート表示】')
for value in sorted(python_list):
    print(value)

print('---------------------------------------')
print('【リストの再表示】')
for value in python_list:
    print(value)
