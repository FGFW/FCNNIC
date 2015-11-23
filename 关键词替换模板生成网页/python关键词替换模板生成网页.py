"""
python关键词替换模板生成网页.py
http://www.bathome.net/thread-37777-1-1.html
依山居 1:07 2015/11/24
→_→强烈鄙视做垃圾站的
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
    html=moban
    #一行代码长到天涯海角~
    html=html.replace("{关键词1}",rkey[0]).replace("{关键词2}",rkey[1]).replace("{关键词3}",rkey[2]).replace("{关键词4}",rkey[3])
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    with open(dirs+"index.htm","w+",encoding="utf-8") as f:
        f.write(html)


