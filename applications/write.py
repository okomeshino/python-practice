fin_sjis = open('applications/read.txt', 'r', encoding='utf-8')
fout_euc = open('applications/euc-jp.txt', 'w', encoding='euc_jp')
fout_utf = open('applications/utf-8.txt', 'w', encoding='utf-8')

for row in fin_sjis:
    fout_euc.write(row)
    fout_utf.write(row)

fin_sjis.close()
fout_euc.close()
fout_utf.close()