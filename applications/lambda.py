# encoding:utf-8
def plus_value(num_1, num_2):
    return num_1 + num_2


print(plus_value(10, 100))

# lambda式は「lambda」のあとに引数を指定し、「:」のあとに処理を記述する
l_func = lambda num_1, num_2: num_1 + num_2
print(l_func(10, 100))
