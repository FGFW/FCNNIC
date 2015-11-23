"""
python读文本中的第一列内容生成BAT文件.py
gayhub https://github.com/FGFW/FCNNIC
http://www.bathome.net/thread-38284-1-1.html
依山居 22:56 2015/11/23
小意思~
"""
import re
with open("moban.bat") as f:
    moban=f.read()
with open("1.txt") as f:
    txt=f.read()
rec=re.compile("(\w{7}\d{5})")
result=re.findall(rec,txt)
for r in result:
    moban=re.sub(rec,r,moban)
    with open(r+".bat","w+") as f:
        f.write(moban)
        f.close()
    
