"""
python3取出重复3次的字符串保存为3列.py
http://bbs.bathome.net/thread-39592-1-1.html
codegay 2016年3月8日 00:56:57

"""

#测试数据
a="""
01 01 01 02 02 02 03 03 03 04 05 05 
04 04 05 04 05 05 06 06 06 07 07 08
07 08 09 07 08 08 07 09 09 10 11 12
"""
with open("a.txt","w+") as f:
    f.write(a)

#python3取出重复3次的字符串保存为3列.py
with open("a.txt") as f:
    txt=f.read().split()

t3=[]
[t3.append(r) for r in txt if (r not in t3) and txt.count(r)>=3]

#N为结果输出为多少列
N=3
r3=[' '.join(t3[r:r+N])+"\n" for r in range(0,len(t3),N)]

print(r3)
with open("out.txt","w+") as f:
    f.writelines(r3)
