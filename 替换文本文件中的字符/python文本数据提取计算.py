"""
python文本数据提取计算.py
http://bbs.bathome.net/thread-39649-1-1.html
codegay 2016年3月11日 23:27:16

"""
import random
import re

#生成测试数据
with open("a.txt","w+") as f:
    [f.write("exp= "+str(random.randint(1,9999))+"\n") for r in range(1,33)]

#读取数据,懒得写正则了，假设数据格式严格：exp= 数值
with open("a.txt") as f:
    txt=[r.split("=")[1].strip() for r in f.readlines()]

results=["exp= "+str(float(r)/4)+"\n" for r in txt]

with open("b.txt","w+") as f:
    f.writelines(results)
    #2016年3月12日 00:11:08
