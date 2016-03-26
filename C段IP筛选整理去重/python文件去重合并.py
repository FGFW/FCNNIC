"""
文件去重合并.py
2016年3月27日 00:34:36 codegay
"""
with open ("1.txt",encoding="utf-8") as f1, open('2.txt',encoding='utf-8') as f2, open('result.txt',"w+",encoding='utf8') as result:
    result.writelines(list(frozenset(f1.readlines()+f2.readlines())))