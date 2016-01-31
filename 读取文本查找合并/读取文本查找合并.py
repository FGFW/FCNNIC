"""
读取文本查找合并1.py
依山居 2016年1月19日 20:09:35
http://bbs.bathome.net/thread-39134-1-1.html
"""
import time
start=time.time()
print("运行中..."*3)
indexlist=[r.strip("\n") for r in open("index.txt")]
ddi=[r.strip("\n") for r in open("DDI.txt")]
for i in indexlist:
    result=i+" "
    for d in ddi:
        if i in d:
            result+=d.split()[1]+" "
        print(result)
            
            
end=time.time()
pt=end-start
print("运行耗时：",pt)
try:
    input("按回车退出")
except SyntaxError:
    pass
