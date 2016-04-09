"""
python获取DNS查询结果.py
http://bbs.bathome.net/thread-39978-1-1.html
2016年4月9日 10:08:16 codegay
"""
import re
import subprocess
host="www.google.com"
txt=subprocess.getoutput("nslookup -qt=AAAA www.google.com 223.5.5.5")

print(txt)

result=re.findall(r"""Address:  ((?:\w*:){5}\w*)""",txt)[0]

print("匹配结果:",result)

with open("result.txt","w+") as f:
    f.write(result+"\t"+host+"\n")

"""
非权威应答:

服务器:  public1.alidns.com
Address:  223.5.5.5

名称:    www.google.com
Address:  2404:6800:4005:801::2004

匹配结果: 2404:6800:4005:801::2004
[Finished in 0.2s]
"""