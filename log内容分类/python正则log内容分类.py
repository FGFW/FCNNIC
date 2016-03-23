"""
python正则log内容分类.py
2016年3月24日 00:54:44 codegay
"""
import re
with open("event_1.log") as f,open("0.log","w+") as f0, open("1.log","w+") as f1:
    for line in f:
        result1=re.findall(r"^[ad]\s+0\s.*$",line,re.S)
        result2=re.findall(r"^[ad]\s+1\s.*$",line,re.S)
        if result1:
            f0.writelines(result1)
        if result2:
            print(result2)
            f1.writelines(result2)

    
