"""
python format替换模板文件中的字符串2.py
问题来源 http://www.bathome.net/thread-37777-1-1.html
几天不写代码，手生...
今天路上看到format和%s替换模板文件的用法。写出来巩固一下。
再来一个format替换的写法。模板文件中的格式为{关键词1},加上python3支持中文变量名，
所以可format(关键词1='xx')的方式替换.
"""
import random
import os

with open("host.txt",encoding="utf-8") as f:
    host=[r.rstrip() for r in f.readlines()]
with open("key.txt",encoding="utf-8") as f:
    key=[r.rstrip() for r in f.readlines()]
with open("moban.txt",encoding="utf-8") as f:
    moban=f.read()

for h in host:
    rkey=random.sample(key,4)
    dirs="./"+h+"/"+"www."+h+"/"
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    with open(dirs+"index.html","w+",encoding="utf-8") as f:
        f.write(moban.format(关键词1=rkey[0],关键词2=rkey[1],关键词3=rkey[2],关键词4=rkey[3]))
