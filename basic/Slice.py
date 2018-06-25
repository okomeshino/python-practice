# coding:utf-8

# スライスは以下のような記述で開始位置、終了位置、ステップ幅を指定する
# 指定の値は省略可能。シーケンスの様相に応じて適切に動作する

# 書式
# sequence[<開始位置>:<終了位置>:<ステップ幅>]

# シーケンス
test_list = ['https', 'www', 'python', 'izm', 'com']

# 一般的なスライス
print(test_list[2:])    # 開始位置の指定（末尾まで）
print(test_list[:4])    # 終了位置の指定（先頭から）
print(test_list[2:4])   # 開始位置と終了位置の指定（2から4まで）
print(test_list[::2])   # ステップ幅の指定（2つごとに取得する）

# 負の数
print(test_list[-1:])   # 末尾から全てのテキスト
print(test_list[:-1])   # 末尾までの全ての要素
print(test_list[::-1])  # 末尾から全ての逆順要素

# 範囲指定が要素数を超過している場合は要素数に応じてカットされる
print(test_list[:999])

# 要素の代入も可能
test_list[1:3] = ('WWW', 'PYTHON')
print(test_list)
