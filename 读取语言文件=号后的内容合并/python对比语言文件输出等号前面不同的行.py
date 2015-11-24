"""
python对比语言文件输出等号前面不同的行.py
http://www.bathome.net/thread-38064-1-2.html
依山居 13:41 2015/11/24
"""
import re
with open("zh_CN.lang",encoding="utf-8") as f:
    zh=f.read()
rec=re.compile("(.+)=(.*)\n")
zht=re.findall(rec,zh)

with open("en_US.lang",encoding="utf-8") as f:
    en=f.read()
    ent=re.findall(rec,en)
    
notinen=[e+"="+c+"\n" for e,c in zht if (e not in en)]
notinzh=[k+"="+v+"\n" for k,v in ent if (k not in zh)]

with open("diff.txt","w+",encoding="utf-8") as f:
    if len(notinen)>=1:
        f.writelines(['zh文件比en文件多出的行:\n']+notinen)
    if len(notinzh)>=1:
        f.writelines(['en文件比zh文件多出的行：\n']+notinzh)
