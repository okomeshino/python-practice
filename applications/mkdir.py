# encoding:utf-8
import os
import shutil


def show_dir(path):
    print('=====================================')
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            print(os.path.join(dirpath, dirname))


tmpDir = '/Users/iinoryo/Documents/Projects/python-practice/tmp'

os.mkdir(tmpDir)
os.makedirs('/Users/iinoryo/Documents/Projects/python-practice/tmp/mkdir1/mkdir2/mkdir3')
show_dir(tmpDir)

os.rmdir('/Users/iinoryo/Documents/Projects/python-practice/tmp/mkdir1/mkdir2/mkdir3')
show_dir(tmpDir)

# os.removedirs(tmpDir)
shutil.rmtree(tmpDir)