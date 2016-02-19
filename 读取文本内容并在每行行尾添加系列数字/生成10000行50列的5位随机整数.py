"""
生成10000行50列的5位随机整数.py
http://www.oschina.net/question/2400361_2151742
2016年2月19日 14:50:52 codegay
"""
import random
with open("10000x50.txt","w+") as f:
    f.write(",".join([str(r) for r in range(1,51)])+"\n")#列名
    for n in range(0,10000):
         rn=','.join([str(random.randint(10000,99999)) for r in range(1,51)])+"\n"
         f.write(rn)
         
input("回车退出")
