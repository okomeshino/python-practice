# encoding:utf-8

# ループ開始前に 1 から 10 まですべてを確保
# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     print(i)

# 呼び出されるごとに値を生成
# for i in <ジェネレーター>:
#     print(i)


def func_sample():
    yield ('おはよう')
    yield ('こんにちは')
    yield ('こんばんは')


for i in func_sample():
    print(i)


# nextで待機になる
f = func_sample()
print(next(f))
print(next(f))
print(f.__next__())


# ジェネレーター式
gen_sample = (i for i in 'おはよう こんにちは こんばんは'.split())

print(gen_sample)
for i in gen_sample:
    print(i)
