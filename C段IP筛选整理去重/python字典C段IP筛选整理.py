"""
python字典C段IP筛选整理.py
题目来源 http://www.bathome.net/thread-38037-1-2.html
依山居 7:16 2015/11/20
字典中的键唯一，所以可以用来去重
"""
字典={}
with open("a.txt") as f:
    txt=f.readlines()
    f.close()
    ip=['.'.join(r.split(".")[0:3]) for r in txt]

for r in ip:
    字典[r]=1
    
for r in 字典:
    print(r+".1")

