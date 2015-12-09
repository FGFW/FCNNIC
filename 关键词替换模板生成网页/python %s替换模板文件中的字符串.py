"""
python %操作符替换模板文件中的字符串.py
6:04 2015/12/10
问题来源 http://www.bathome.net/thread-37777-1-1.html
几天不写代码，手生...
今天路上看到format和%s替换模板文件的用法。写出来巩固一下。
"""
import random
import os

#先把模板中需要替换的地方改成:%(关键词1)s这样的格式
moban="""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

<head>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<title>%(关键词1)s%(关键词2)s%(关键词3)s%(关键词4)s</title>

<meta name="keywords" content="%(关键词1)s%(关键词2)s%(关键词3)s%(关键词4)s" />

<meta name="description" content="%(关键词1)s努力打造%(关键词2)s影视导航系统为最好的%(关键词3)s影视系统!" />

</head>

上下标签比如关键词1要一样。

<li>Copyright © 2015 %(关键词1)s all rights reserved.  <a href="/detail/map.html" target="_blank">网站地图</a></li>

</body>

</html>
"""

with open("host.txt",encoding="utf-8") as f:
    host=[r.rstrip() for r in f.readlines()]
with open("key.txt",encoding="utf-8") as f:
    key=[r.rstrip() for r in f.readlines()]

for h in host:
    rkey=random.sample(key,4)
    关键词={"关键词"+str(r+1):rkey[r] for r in range(len(rkey))}
    dirs="./"+h+"/"+"www."+h+"/"
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    with open(dirs+"index.html","w+",encoding="utf-8") as f:
        f.write(moban %关键词)
