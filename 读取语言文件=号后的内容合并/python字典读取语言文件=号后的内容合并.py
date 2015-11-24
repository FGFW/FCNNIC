"""
python字典读取语言文件=号后的内容合并.py
题目来源 http://www.bathome.net/thread-38064-1-2.html
依山居 10:54 2015/11/24
使用python字典合并内容,不能保持原文件的顺序~
"""
with open("zh_CN.lang",encoding="utf-8") as f:
    zh=[r.rstrip().split("=") for r in f.readlines() if "=" in r ]
zh={r[0]:r[1] for r in zh}

with open("en_US.lang",encoding="utf-8") as f:
    en=[r.split("=") for r in f.readlines() if "=" in r ]
en={r[0]:r[1] for r in en}

for r in zh:
    if (zh[r]!=''):
        en[r]=zh[r]

result=sorted([r+"="+en[r]+'\n' for r in en])
with open("out.txt","w+",encoding="utf-8") as f:
    f.writelines(result)
    f.close()


