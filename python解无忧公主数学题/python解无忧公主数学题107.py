"""
python解无忧公主数学题107.py
http://mp.weixin.qq.com/s?__biz=MzI5ODEwMDQyNw==&mid=402343371&idx=1&sn=0de458a3653a0070ba3912bda7d01db9&scene=25#wechat_redirect
2016年3月9日 12:49:55 codegay
"""
def ff1():
    #用程序自动把index对应位置的数字切出来。
    exp=990*991*992*993
    s="966428A91B40"
    #问AB=多少
    ab=str(exp)[s.index("A")]+str(exp)[s.index("B")]
    print("方法1: AB =",ab)
    #2016年3月9日 13:03:02 
ff1()


def ff2(exp=996*997*998*999,s="9900x4yz0024"):
    #2016年3月11日 13:32:03
    #本函数目的设计成可以用来解同类题型，输入一个表达式，算出其结果部分被字母打码的值。
    abc=''.join([r for r in s if r.isalpha()])
    v=''.join([str(exp)[s.index(r)] for r in s if r.isalpha()])
    print("方法2结果:",abc,"=",v)
    #2016年3月11日 14:11:58
ff2()
    
