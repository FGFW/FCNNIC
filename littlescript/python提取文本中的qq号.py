"""
python
2016年4月1日 01:05:09 codegay
"""
import re
txt=open("qq.txt").read()
result=re.findall(r"""&Uin=(\d+)""",txt)
print(result)