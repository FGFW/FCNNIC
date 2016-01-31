"""
读取文本查找合并.py
依山居 2016年1月19日 20:09:35
http://bbs.bathome.net/thread-39134-1-1.html
"""
import re
import time
start=time.time()
print("运行中..."*3)
index=open("index.txt").read()
indexlist=re.findall(r"DB\d+",index)
DDI=open("DDI.txt").read()
with open("out.txt","w+") as f:
    for r in indexlist:
        DDIlist=re.findall(r"%s.*(DB\d+)" % r,DDI)
        f.write(r+' '+' '.join(DDIlist)+"\n")

end=time.time()
pt=end-start
print("运行耗时：",pt)
try:
    input("按回车退出")
except SyntaxError:
    pass
