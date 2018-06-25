# encoding:utf-8

# 基本的なwhile文
counter = 0

while counter < 10:
    counter += 1
    print(counter)

# 無限ループ
while True:
    counter += 1
    print(counter)
    if counter == 10:
        break
