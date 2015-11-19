"""
python正则处理DEL文件换行问题
http://www.bathome.net/thread-38164-1-1.html
依山居 20:38 2015/11/18
参考了网上的资料，python 读取文件默认使用通用模式，不管\r\n都会被转换成\n
所以正则可以简化(\n)，预计可以小幅提高处理速度
"""
import re
import time
start=time.time()

of="a.txt"
rec=re.compile('(\"?)(\n)([^\"])')
with open(of) as f:
    txt=f.read()
    res=re.sub(rec,r'\1\3',txt)
    f.close()

with open("out.txt","w+") as f:
    f.write(res)
    f.close()

end=time.time()
pt=end-start
print("运行耗时：",pt)
try:
    input("按回车退出")
except SyntaxError:
    pass
