# encoding:utf-8
import os

for env in os.environ:
    print(env)

print('-----------------------------------')
print(os.environ.get('windir'))
