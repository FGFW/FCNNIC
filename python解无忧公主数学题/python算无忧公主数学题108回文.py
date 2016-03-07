"""
python解无忧公主数学题108回文.py
题目来源: http://mp.weixin.qq.com/s?__biz=MzI5ODEwMDQyNw==&mid=402360973&idx=1&sn=31014f87b8e65c9cd1d40c625c9c3d90&3rd=MzA3MDU4NTYzMw==&scene=6#rd
2016年3月7日 14:59:17 codegay
"""

#利用到了集合的特性，进行集合交集运算
#2016年3月8日 05:59:41
def 方法1():
    f=lambda x,y: x if str(x*y)==str(x*y)[::-1] else None
    x91={f(r,91) for r in range(1,100) if f(r,91)}
    x93={f(r,93) for r in range(1,100) if f(r,93)}
    x95={f(r,95) for r in range(1,100) if f(r,95)}
    x97={f(r,97) for r in range(1,100) if f(r,97)}
    print("方法1结果:",x91&x93&x95&x97)
    return (x91&x93&x95&x97)

方法1()

#2016年3月8日 06:23:32
def ff2():
    
    def f(x,y):
        if str(x*y)==str(x*y)[::-1]:
            return x
        
    results=[r for r in range(1,100) if f(r,91) and f(r,93) and f(r,95) and f(r,97)]
    print("方法2结果:",results)
    #2016年3月8日 06:40:33
    return results

ff2()
        
