# encoding:utf-8

# セットの比較
test_set_1 = set({'python', '-', 'izm', '.', 'com'})

# isdisjoint 共通の要素を持たない時にTrue
print(test_set_1.isdisjoint({'python', 'izm'}))
print(test_set_1.isdisjoint({1, 2, 3}))

print('------------------------------------------')

# issubset セットの全要素が引数の反復可能オブジェクトに含まれている時にTrue
print(test_set_1.issubset({'python', 'izm'}))
print(test_set_1.issubset({'www', 'python', '-', 'izm', '.', 'com'}))

print('------------------------------------------')

# issuperset 引数の反復可能オブジェクトの全要素がセットに含まれている時にTrue
print(test_set_1.issuperset({'python', 'izm'}))
print(test_set_1.issubset({'www', 'python', '-', 'izm', '.', 'com'}))

print('------------------------------------------')

# セットを比較して作成
test_set_2 = {'python', 'izm', 'com'}

# union セットと引数の反復可能オブジェクトのすべての要素を持つセットを作成
print(test_set_2.union({'python', 'www'}))
# intersection セットと引数の反復可能オブジェクトとの間における共通の要素を新たなセットとして作成
print(test_set_2.intersection({'python', 'www'}))
# difference セットに含まれていて引数の反復可能オブジェクトとには含まれない要素を持つ新たなセットを作成
print(test_set_2.difference({'python', 'www'}))
# symmetric_difference セットと引数の反復可能オブジェクトのどちらかだけに含まれる要素を持つ新たなセットを作成
print({'python', 'www'})

print('------------------------------------------')

# セットを比較して更新
test_set_3 = {'python', 'izm', 'com'}
test_set_3.intersection_update({'python', 'www'})
print(test_set_3)

test_set_3 = {'python', 'izm', 'com'}
test_set_3.difference_update({'python', 'www'})
print(test_set_3)

test_set_3 = {'python', 'izm', 'com'}
test_set_3.symmetric_difference_update({'python', 'www'})
print(test_set_3)
