"""
python正则替换语言文件=号后的内容合并.py
http://www.bathome.net/thread-38064-1-2.html
依山居 12:29 2015/11/24
这个版本使用正则匹配替换
使用cn文件中已有的内容，正则替换en文件内容输出到out.txt
out.txt保持了en文件的顺序
"""
import re
with open("zh_CN.lang",encoding="utf-8") as f:
    zh=f.read()
rec=re.compile("(.+)=(.*)\n")
zht=re.findall(rec,zh)

with open("en_US.lang",encoding="utf-8") as f:
    en=f.read()

for e,c in zht:
    rec=re.compile("(%s)=(.*)\n" %e)
    en=re.sub(rec,r"\1=%s\n" %c,en)

with open("out.txt","w+",encoding="utf-8") as f:
    f.write(en)
    f.close()
