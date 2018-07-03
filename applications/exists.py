# encoding:utf-8
import os

filePath = '/Users/iinoryo/Documents/Projects/python-practice'

print(filePath)

if os.path.exists(filePath):
    print('指定のファイル、またはディレクトリが存在しています。')

    if os.path.isfile(filePath):
        print('指定のパスはファイルです.')

    if os.path.isdir(filePath):
        print('指定のパスはフォルダです。')

else:
    print('指定のファイル、またはディレクトリが存在していません。')
