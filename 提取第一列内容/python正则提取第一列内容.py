"""
python正则提取第一列内容
依山居 22:35 2015/11/17
http://www.bathome.net/thread-38181-1-1.html
"""
import re
rec=re.compile("^(00[\w]{6})")
with open("a.txt") as f:
    txt=f.readlines()
    res=[''.join(re.findall(rec,l))+"\n" for l in txt]
with open("out1.txt","w+") as f:
    f.writelines(res)
