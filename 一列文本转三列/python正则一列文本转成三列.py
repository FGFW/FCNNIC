"""
python正则表达式一列文本转成三列.py
依山居 8:18 2015/11/12
总结，我自己生成了百万行来测试，文本文件8M大，内容为1-999999
运行耗时1秒左右
"""
print("运行中..."*3)
import re
import time
start=time.time()

out=open("out.txt","w+")
reg=re.compile(r"(.*)\n(.*)\n(.*)\n")
with open("a.txt") as f:    
    txt=f.read()
    f.close()
result=re.sub(reg,r"\1  \2  \3\n",txt)
#print(result)
out.write(result)
out.close()

end=time.time()
pt=end-start
print("运行耗时：",pt)
try:
    input("按回车退出")
except SyntaxError:
    pass

