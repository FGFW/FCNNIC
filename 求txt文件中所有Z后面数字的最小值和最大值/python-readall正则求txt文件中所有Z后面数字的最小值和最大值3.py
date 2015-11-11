#python正则求txt文件中所有Z后面数字的最小值和最大值3
#依山居 10:57 2015/11/11
#题目来源: http://www.bathome.net/thread-38027-1-1.html

#这个版本使用read()直接读入整个文件内容然后正则匹配.
#经过测试比逐行处理，速度快了3-5倍
#总结：一次性读入正则匹配整个文件内容，处理速度快了3-5倍。
#要不是自己起心生成数据来测试，就被带到沟里了。

import time
start=time.time()

import re
def ftxt(txt="b.txt"):
        #global zl
        zl=[]
        reg=re.compile("Z(-?\d*\.?\d*)")
        with open(txt) as f:
                c=f.read()
                regresult=re.findall(reg,c)
                if regresult:
                        for r in regresult:
                                zl.append(float(r))                            
        return zl
        
zl=ftxt()
print("list长度: ",len(zl))
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

end=time.time()
pt=end-start
print("程序运行时间：",pt)
try:
    input("按回车退出")
except SyntaxError:
    pass

"""
输出:
list长度:  1921678
大:  999.0
小:  -99.0
小:  -99.0
大：  999.0
程序运行时间： 7.053403377532959
"""
