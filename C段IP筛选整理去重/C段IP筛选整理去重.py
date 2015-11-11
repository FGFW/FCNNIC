"""
C段IP筛选整理去重.PY
依山居 16:04 2015/11/11
吐槽，这题本质是个去重处理。我写了半天没写出来。
题目来源： http://www.bathome.net/thread-38037-1-2.html
"""
import time
start=time.time()

with open("a.txt","r") as f:
    txt=f.read()
    ll=[]
    ip=txt.rsplit()
    for l in ip:
        l=l.split(".")
        l[-1]="1"
        joinl=".".join(l)
        if (joinl not in ll):
           ll.append(joinl)
           print(joinl)

end=time.time()
pt=end-start
print("程序运行时间：",pt)
try:
    input("按回车退出")
except SyntaxError:
    pass

"""
输出：
192.168.1.1
192.168.2.1
192.168.5.1
192.168.6.1
192.168.9.1
192.169.3.1
程序运行时间： 0.022000789642333984
"""
