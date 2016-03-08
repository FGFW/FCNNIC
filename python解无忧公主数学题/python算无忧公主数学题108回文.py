"""
python解无忧公主数学题108回文.py
题目来源: http://mp.weixin.qq.com/s?__biz=MzI5ODEwMDQyNw==&mid=402360973&idx=1&sn=31014f87b8e65c9cd1d40c625c9c3d90&3rd=MzA3MDU4NTYzMw==&scene=6#rd
2016年3月7日 14:59:17 codegay

"""

#利用到了集合的特性，进行集合交集运算
#2016年3月8日 05:59:41
def 方法1():
    f=lambda x,y: str(x*y)==str(x*y)[::-1]
    x91={r for r in range(1,100) if f(r,91)}
    x93={r for r in range(1,100) if f(r,93)}
    x95={r for r in range(1,100) if f(r,95)}
    x97={r for r in range(1,100) if f(r,97)}
    print("方法1结果:",x91&x93&x95&x97)
    return (x91&x93&x95&x97)

方法1()

#2016年3月8日 06:23:32
def ff2():
    
    def f(x,y):
        return str(x*y)==str(x*y)[::-1]
        
    results=[r for r in range(1,100) if f(r,91) and f(r,93) and f(r,95) and f(r,97)]
    print("方法2结果:",results)
    #2016年3月8日 06:40:33
    return results

ff2()
        
#2016年3月8日 06:59:08
#用正则匹配写一个
import re
def ff3():
    def f(x,y):
        return re.match(r"""^(\d?)(\d?)(\d?)(\d?)\4\3\2\1$""",str(x*y))

    x91=[r for r in range(1,100) if f(r,91)]
    results=[r for r in x91 if f(r,93) and f(r,95) and f(r,97)]
    print("方法3结果:",results)
    #2016年3月8日 07:29:33

ff3()

#2016年3月8日 08:39:02
#再尝试改进一下写法
def ff4():
    l=[91,93,95,97]
    #
    f=lambda x,iters: False not in [str(x*r)==str(x*r)[::-1] for r in iters]
    results=[r for r in range(1,100) if f(r,l)]
    print("方法4结果:",results)
    #2016年3月8日 09:17:07
ff4()
    
