"""
如何随机生成1到999999999之间的数字.py
http://bbs.bathome.net/thread-39410-1-1.html
2016年2月19日 01:56:51 codegay
"""

import time
import random
start=time.time()
print("运行中..."*3)

txt={str(random.randint(1000000001,2000000000))[1:]+"\n" for r in range(10000000)}#集合解析生成一千万随机数并去重。会导致比列表解析慢上6秒左右。运行耗时： 44
print(len(txt))
with open("sj.txt","a+") as f:
    f.writelines(txt)

end=time.time()
pt=end-start
print("运行耗时：",pt)
try:
    input("按回车退出")
except SyntaxError:
    pass
