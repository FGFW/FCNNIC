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
