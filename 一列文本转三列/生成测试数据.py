"""
生成一列x行文本
依山居 16:32 2015/11/11
"""
import time
start=time.time()

out=open("a.txt","a+")
for r in range(1000000):
    out.write(str(r)+"\n")
out.close()

end=time.time()
pt=end-start
print("运行耗时：",pt)
try:
    input("按回车退出")
except SyntaxError:
    pass
