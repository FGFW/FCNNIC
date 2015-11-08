#python正则求txt文件中所有Z后面数字的最小值和最大值
#依山居 2:23 2015/11/8
#题目来源: http://www.bathome.net/thread-38027-1-1.html
#这个版本改用正则表达式处理文本.

import re
def ftxt(txt="a.txt"):
        #global zl
        zl=[]
        reg=re.compile("Z(-?\d*\.?\d*)")
        with open(txt) as f:
                for line in f:
                        regresult=re.findall(reg,line)
                        if regresult:
                                for r in regresult:
                                        zl.append(float(r))
        print(len(zl))
        return zl
        
zl=ftxt()
print(zl)
#方法一：使用python内建的max min函数
print("大: ",max(zl))
print("小: ",min(zl))
#方法二： 使用sorted排序后取首位和末尾元素。
#还可以用zl.sort(reverse=True) zl.reverse() 排序
zl=sorted(zl)
print("小: ",zl[0])
print("大： ",zl[-1])
#总结是不管是max 还是sort 比较的对象都应该统一是数字。
#所以处理前需要先丢掉字母Z并转成浮点数。
try:
    input("执行完成,按回车退出")
except SyntaxError:
    pass
"""
输出:
11
[19.429, -14.477, -14.77, -15.012, -15.312, -16.012,
-50.013, 30.0, -14.977, -15.012, -15.012]
大:  30.0
小:  -50.013
小:  -50.013
大：  30.0
"""
