"""
python解字迷abc+def=ghij.py
2016年4月1日 06:43:46 codegay
参考资料: http://bbs.emath.ac.cn/thread-3023-1-1.html
无脑暴力
"""
from itertools import permutations
result=[]
for r in permutations(range(10)):
    a,b,c,d,e,f,g,h,i,j=r
    abc=a*100+b*10+c
    if abc>=100:
        deff=d*100+e*10+f
        if deff>=100:
            ghij=g*1000+h*100+i*10+j
            if 1000<=ghij<10000 :
                if ghij==abc+deff:
                    if len(set(str(ghij)))==len(str(ghij)):
                        result.append(ghij)
print("一共?:",len(result))
print("ghij最大:",max(result))
#一共?: 96
#ghij最大: 1602
#[Finished in 5.7s]

