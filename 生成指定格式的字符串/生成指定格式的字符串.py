"""
生成指定格式的字符串.py
http://bbs.bathome.net/thread-39829-1-1.html
2016年3月27日 21:46:41  codegay
"""
import time
start=time.time()
print("运行中..."*3)

#这是生成aabcbc格式字符串
import itertools
from itertools import product
ss='abcdefghijklmnopqrstuvwxyz0123456789'
with open("result.txt","w+") as f:
    for r in product(ss,ss,ss,ss,ss,ss):
        #       aa             bc            bc
        if r[0]==r[1] and r[2]==r[4] and r[3]==r[5]:
            s=''.join(r)
            #print(s)
            f.write(s+"\n")


    
    
end=time.time()
pt=end-start
print("运行耗时：",pt)

input()
