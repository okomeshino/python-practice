# encoding:utf-8
import csv


# カスタムしたフォーマットを追加できる
class CustomFormat(csv.excel):
    quoting = csv.QUOTE_ALL


csv.register_dialect('myformat', CustomFormat)


csv_file = open('./python.csv', 'w', newline='')

# writer = csv.writer(
#     csv_file,
#     dialect=CustomFormat()
# )

# 独自のフォーマットを登録できる
writer = csv.writer(
    csv_file,
    dialect='myformat'
)


# 独自のフォーマットを記述できる
# writer = csv.writer(
#     csv_file,
#     quoting=csv.QUOTE_ALL,
#     delimiter=':',
#     quotechar='`'
# )

# 用意されているCSVフォーマット
# writer = csv.writer(
#     csv_file,
#     dialect=csv.excel_tab
# )


row = ('python', '-', 'izm', '1')
writer.writerow(row)

rows = []
rows.append(('python', '-', 'izm', '2'))
rows.append(('python', '-', 'izm', '3'))
rows.append(('p,y,t,h,o,n', '-', 'i,z,m', '4'))
writer.writerows(rows)

csv_file.close()
