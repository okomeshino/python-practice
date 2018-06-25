# encoding:utf-8

# 10を引数で渡す → 10回ループ
for i in range(10):
    print(i)
    if i == 9:
        print("------------------------------")

# 2と10を引数で渡す → 2から始まって9までループ
for i in range(2, 10):
    print(i)
    if i == 9:
        print("------------------------------")

# 負の数を渡すことも可能
for i in range(-2, 10):
    print(i)

