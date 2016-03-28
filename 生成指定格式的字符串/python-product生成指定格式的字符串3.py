"""
python-product生成指定格式的字符串3.py
http://bbs.bathome.net/thread-39829-1-1.html
2016年3月29日 04:51:38  codegay
改了下思路,速度快了非常多,前面的程序需要5百秒,这个只需要0.2s
"""
#这是生成aabcbc格式字符串
from itertools import product
ss='abcdefghijklmnopqrstuvwxyz0123456789'
with open("result.txt","w+") as f:
    for a,b,c in product(ss,ss,ss):
        f.write(a+a+b+c+b+c+"\n")
