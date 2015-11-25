"""
python正则匹配肇事车牌照号
http://www.bathome.net/thread-16242-1-1.html
依山居 4:50 2015/11/25
"""
import re
aabb=["%d*%d=%d" %(r,r,r*r) for r in range(1,100)]
aabb=str(aabb)
result=re.findall(r"(\d)\1\*\1\1=(\d)\2(\d)\3",aabb)
[print(b*2+c*2) for a,b,c in result]
#正则还能这样写
print(re.sub(r".*=(\d)\1(\d)\2.*",r"\1\1\2\2\n",aabb))
