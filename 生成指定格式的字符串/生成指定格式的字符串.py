"""
生成指定格式的字符串.py
http://bbs.bathome.net/thread-39829-1-1.html
2016年3月27日 21:46:41  codegay
"""
#这是生成aabcbc的
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
