"""
python format替换模板文件中的字符串3.py
问题来源 http://www.bathome.net/thread-37777-1-1.html
几天不写代码，手生...
今天路上看到format和%s替换模板文件的用法。写出来巩固一下。
"""
import random
import os

#先把模板中需要替换的地方改成:{关键词[0]}这样的格式，就可以直接用format直接替换。
moban="""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

<head>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<title>{关键词[0]}{关键词[1]}{关键词[2]}{关键词[3]}</title>

<meta name="keywords" content="{关键词[0]}{关键词[1]}{关键词[2]}{关键词[3]}" />

<meta name="description" content="{关键词[0]}努力打造{关键词[1]}影视导航系统为最好的{关键词[3]}影视系统!" />

</head>

上下标签比如关键词1要一样。

<li>Copyright © 2015 {关键词[0]} all rights reserved.  <a href="/detail/map.html" target="_blank">网站地图</a></li>

</body>

</html>
"""

with open("host.txt",encoding="utf-8") as f:
    host=[r.rstrip() for r in f.readlines()]
with open("key.txt",encoding="utf-8") as f:
    key=[r.rstrip() for r in f.readlines()]

for h in host:
    dirs="./"+h+"/"+"www."+h+"/"
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    with open(dirs+"index.html","w+",encoding="utf-8") as f:
        f.write(moban.format(关键词=random.sample(key,4)))
