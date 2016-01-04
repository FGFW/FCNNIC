"""
读取文本内容并在每行行尾添加系列数字.py
http://www.bathome.net/thread-38881-1-1.html
依山居 2016年1月4日 20:53:41
完全逐行处理再逐行写入
"""
import time
start=time.time()
print("运行中..."*3)

#生成0000-9999，用了楼上的思路
sq=[str(r)[1:]+"\n" for r in range(10000,20000)]

with open("数据.txt") as fa,open("result.txt","a+") as fb:
    for l in fa:
        sn=l.rstrip()
        for s in sq:
            fb.write(sn+s) 
            
end=time.time()
pt=end-start
print("运行耗时：",pt)
try:
    input("按回车退出")
except SyntaxError:
    pass
"""
数据.txt一万行129-143秒
result.txt 1.2GB
我了个去，发生了什么。逐行处理再逐行写入反而比较快。
"""
