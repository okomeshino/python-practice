# encoding:utf-8
test_dict = {}

# dictionaryは追加順を保持してはくれない
test_dict['word'] = 'doc'
test_dict['excel'] = 'xls'
test_dict['access'] = 'mdb'
test_dict['powerpoint'] = 'ppt'
test_dict['notepad'] = 'txt'
test_dict['python'] = 'py'

for key in test_dict:
    print(key)

print('-----------------------------')

# collections.OrderdDict()は追加順を保持する
import collections

test_ordered_dict = collections.OrderedDict()

test_ordered_dict['word'] = 'doc'
test_ordered_dict['excel'] = 'xls'
test_ordered_dict['access'] = 'mdb'
test_ordered_dict['powerpoint'] = 'ppt'
test_ordered_dict['notepad'] = 'txt'
test_ordered_dict['python'] = 'py'

for key in test_ordered_dict:
    print(key)
