"""
python正则版读取文本内容并在每行行尾添加系列数字.py
http://www.bathome.net/thread-38881-1-1.html
依山居 2016年1月4日 11:09:51
"""
import re
import time
start=time.time()
print("运行中..."*3)

#生成0000-9999序列
sq=''.join([str(r).zfill(4)+"\n" for r in range(0,10000)])

#或者直接取前前面脚本的生成好的序列
#with open("序列.txt") as f:
#   sq=f.read()

with open("数据.txt") as f:
    data=f.readlines()
    
for r in data:
    result=re.sub('(\d+)',r'%s\1' % r.rstrip(),sq)
    with open("result.txt","a+") as f:
        f.write(result)
end=time.time()
pt=end-start
print("运行耗时：",pt)
try:
    input("按回车退出")
except SyntaxError:
    pass

"""
测试数据为一万行数时，得到的文本为1.2GB
处理时间大约是182秒。
"""
