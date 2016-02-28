"""
获取重复的行并且重复的行只保留一次.py
http://bbs.bathome.net/thread-39502-1-1.html
2016年2月28日 03:57:29 codegay
通过help(list),可见python序列有count方法.
-_-基础教程应该有说到的，估计是学过就忘记了.
python3
"""
#a.txt内容必须是任意但是有重复行的内容。
#我使用的是一列IP地址进行测试的.
with open("a.txt") as f:
    txt=f.readlines()

#方法一 集合解析,缺点集合无序，不会保持原来的先后顺序
results={r for r in txt if (txt.count(r) >= 2)}
print("一：",results)

#方法二 map filter lambda ,
b=[]
a=map(lambda y:b.append(y) if (y not in b) else None,filter(lambda x:(txt.count(x) >= 2),txt))
list(a)#python3中map等函数返回成生成器,需要list或者for 历遍到的时候才进行计算结果。
print("二:",b)

#方法三
l2=[r for r in txt if txt.count(r)>=2]
result3=[]
[result3.append(r) for r in l2 if r not in result3]
print("三:",result3)

#方法4 字典 不保持原先后顺序
dd={r:txt.count(r) for r in txt}
ll=[k for k,v in dd.items() if v>=2]
print("4",ll)
