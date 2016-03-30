"""
python解无忧公主的数学时间105 每日一题.py
https://mp.weixin.qq.com/s?__biz=MzI5ODEwMDQyNw==&mid=402334147&idx=1&sn=b4d7342f4375d832cceb4de4ee74ecb3
2016年3月30日 03:30:29 codegay
参考资料 https://www.wolframcloud.com/objects/01b74b78-aef6-4413-b140-108e40b2068c
"""
def ff1():
    d={}
    f=o=r=t=y=t=e=n=s=i=x=0
    for f in range(10000,100000):
        for t in range(100,1000):
            s=f+t*2 #SIXTY=f+t*2
            fT=f/10%10
            tT=t//100
            sT=s/10%10
            fY=f%10
            sY=s%10
            if s<99999 and fY==sY and fT==tT==sT:
                print(s)
#ff1()

def ff2():
    from itertools import permutations
    for h in permutations([g for g in range(10)]):
        f,o,r,t,y,e,n,s,i,x=h
        if len(h) ==len(set(h)) and (f != 0) and (t != 0) and (s !=0):
            forty=f*10000+o*1000+r*100+t*10+y
            ten=t*100+e*10+n
            sixty=s*10000+i*1000+x*100+t*10+y
            if forty+ten*2==sixty:
                print("105结果:T==",t)
#8
#[Finished in 6.7s]
ff2()
