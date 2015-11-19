"""
python正则处理DEL文件换行问题
http://www.bathome.net/thread-38164-1-1.html
依山居 20:38 2015/11/18
"""
import re
import time
start=time.time()

of="a.txt"
rec=re.compile('(\"?)(\r|\n|\r\n)([^\"])')
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
