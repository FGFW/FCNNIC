"""
python-for迭代生成指定格式的字符串2.py
http://bbs.bathome.net/thread-39829-1-1.html
2016年3月29日 04:51:38  codegay
改了下思路,速度快了非常多,前面的程序需要5百秒,这个只需要0.2s
"""
import time
start=time.time()
print("运行中..."*3)

#这是生成aabcbc格式字符串
import itertools
from itertools import product
ss='abcdefghijklmnopqrstuvwxyz0123456789'
with open("result.txt","w+") as f:
    for a in ss:
        for b in ss:
            for c in ss:
                #print(a+a+b+c+b+c)
                f.write(a+a+b+c+b+c+"\n")



end=time.time()
pt=end-start
print("运行耗时：",pt)

#input()
