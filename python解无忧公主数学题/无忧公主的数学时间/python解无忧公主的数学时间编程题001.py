"""
python解无忧公主的数学时间编程题001.py
http://mp.weixin.qq.com/s?__biz=MzI5ODEwMDQyNw==&mid=402273249&idx=4&sn=aa2e79e154a13c5c94673d9a53e49c96&scene=24&srcid=0323mNu08KMNzbVyn7EbUN1d#rd
2016年3月31日 05:16:39 codegay
0-9组成的字典序第一百万个是多少?
"""
from itertools import permutations

#方法1 使用enumerate()当作计数器,只取第一百万个数字.
result=[''.join([str(r) for r in v]) for k,v in enumerate(permutations(range(10)),1) if k==1000000]
print(result)
#['2783915460']
#[Finished in 0.6s]

#方法2 穷举后排序,取出一百万个数字.
result=[''.join([str(r) for r in v]) for k,v in enumerate(permutations(range(10)),1)]
result.sort()
print(result[1000001])
#2783915640
#[Finished in 14.2s]