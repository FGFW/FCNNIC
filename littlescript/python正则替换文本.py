"""
python正则替换文本.py
http://bbs.bathome.net/thread-39523-1-1.html
2016年2月29日 22:52:19 codegay

"""
import re
txt=re.sub(r"\'\)\.Num\(.+","",open("1.txt").read())
print(txt)