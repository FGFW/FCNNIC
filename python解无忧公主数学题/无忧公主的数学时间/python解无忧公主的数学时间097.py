"""
python解无忧公主的数学时间097.py
codegay 2016年3月30日 00:17:26
http://mp.weixin.qq.com/s?__biz=MzI5ODEwMDQyNw==&mid=402225879&idx=1&sn=6ea8e1d5e6a2520ad65eb2713a98af6e&3rd=MzA3MDU4NTYzMw==&scene=6#rd
"""
from itertools import product
n=[[h for h in range(1,7+1)] for r in range(5)]
f=lambda x:x[1]>x[0] and x[1]>x[2] and x[3]>x[2] and x[3]>x[4] and len(set(x))==5
x={r for r in product(*n) if f(r)}
print("097结果:",len(x))
#336
#[Finished in 0.1s]
