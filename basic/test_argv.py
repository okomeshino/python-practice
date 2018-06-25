# coding:utf-8

# 実行コマンド
# 引数を指定
# python test_argv.py python izm com

import sys

args = sys.argv

print(args)
print('第1引数' + args[1])
print('第2引数' + args[2])
print('第3引数' + args[3])
