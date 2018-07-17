# encoding:utf-8
import zipfile

# 複数のファイルをまとめる(ファイルサイズの圧縮は行わない)
zipFile = zipfile.ZipFile('./compress_1.zip', 'w', zipfile.ZIP_STORED)
zipFile.write('./python.py')
zipFile.write('./python.txt')
zipFile.write('./python.csv')
zipFile.close()

# ファイルサイズを圧縮して複数のファイルをまとめる
zipFile = zipfile.ZipFile('./compress_2.zip', 'w', zipfile.ZIP_DEFLATED)
zipFile.write('./python.py')
zipFile.write('./python.txt')
zipFile.write('./python.csv')
zipFile.close()
