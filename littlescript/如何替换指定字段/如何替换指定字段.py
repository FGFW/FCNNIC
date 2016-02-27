"""
如何替换指定字段.py
http://bbs.bathome.net/thread-39434-1-1.html
2016年2月20日 14:51:20 codegay
"""
#方法1
with open("a.txt","r+") as f:
    txt=[r.rstrip("\n").split("-")[0]+"---123\n" for r in f.readlines()]
    print(txt)
    f.seek(0)
    f.truncate()
    [f.write(r) for r in txt]
    print(txt)

#方法2 正则表达式
#2016年2月20日 15:50:15
import re 
with open("b.txt","r+") as f:
    txt=re.sub(r"(.+?)---.+",r"\1---1234",f.read())
    print(txt)
    f.seek(0)
    f.truncate()
    f.write(txt)
    

