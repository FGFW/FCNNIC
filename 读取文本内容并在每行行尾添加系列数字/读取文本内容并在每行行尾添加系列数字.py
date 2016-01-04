"""
读取文本内容并在每行行尾添加系列数字.py
http://www.bathome.net/thread-38881-1-1.html
依山居 2016年1月4日 20:13:28
"""
import time
start=time.time()
print("运行中..."*3)

#生成0000-9999，用了楼上的思路
sq=[str(r)[1:] for r in range(10000,20000)]

with open("数据.txt") as f:
    for l in f.readlines():
        with open("result.txt","a+") as f:
            f.writelines([l.rstrip()+s+"\n" for s in sq])

end=time.time()
pt=end-start
print("运行耗时：",pt)
try:
    input("按回车退出")
except SyntaxError:
    pass
"""
数据.txt一万行152秒
result.txt 1.2GB
每成生一万行结果再写入文件
"""
