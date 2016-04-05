"""
无忧公主的数学时间134.py
http://mp.weixin.qq.com/s?__biz=MzI5ODEwMDQyNw==&mid=403013919&idx=2&sn=7439014ae0182cb4b0222fc2234b34c3&3rd=MzA3MDU4NTYzMw==&scene=6#rd
2016年4月5日 21:46:24 codegay
求正整数n的因数之和的因数之和.
"""
#输入一个正整数n,返回n因数之和的因数之和.也就是2次求因数之和
def factorsx(n,x=2):#x为进行求因素之和的次数
    #def f(n):return sum([r for r in range(1,n+1) if n%r==0])#返回N的因数之和
    #f=lambda n:sum([r for r in range(1,n+1) if n%r==0])#等效写法
    f=lambda n:n+sum([r for r in range(1,n//2+1) if n%r==0])#-_-假装优化一下
    for r in range(x):
        n=f(n)
    print(n)
    return n
factorsx(11)






