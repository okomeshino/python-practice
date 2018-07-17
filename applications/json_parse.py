# encoding:utf-8
import json

json_data = {'Python':'python-izm.com',
             'SearchEngine':('google.co.jp', 'yahoo.co.jp')}

print(type(json_data))

# 普通に変換
# encode_json_data = json.dumps(json_data)

# 見やすい形で変換
encode_json_data = json.dumps(json_data, indent=4)

print(encode_json_data)
print(type(encode_json_data))

print('---------------------------------------------')

# Pythonオブジェクトに変換
encode_json_python_data = json.dumps(json_data)
decode_json_python_data = json.loads(encode_json_python_data)

print(decode_json_python_data)
print(type(decode_json_python_data))