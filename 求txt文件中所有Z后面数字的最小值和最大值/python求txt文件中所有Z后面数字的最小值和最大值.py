#python求txt文件中所有Z后面数字的最小值和最大值
#依山居 19:04 2015/11/7
#题目来源: http://www.bathome.net/thread-38027-1-1.html

zl=[]
with open("a.txt") as f:
        for l in f:
                txtline=l.rsplit()
                for ll in txtline:
                        #print(ll)
                        if ll[0]=="Z":
                                x=float(ll[1:])
                                zl.append(x)
                                
#方法一：使用python内建的max min函数
print("大: ",max(zl))
print("小: ",min(zl))
#方法二： 使用sorted排序后取首位和末尾元素。
zl=sorted(zl)
print("小: ",zl[0])
print("大： ",zl[-1])

#总结是不管是max 还是sort 比较的对象都应该统一是数字。
#所以处理前需要先丢掉字母Z并转成浮点数。
try:
    input("Press enter to continue")
except SyntaxError:
    pass
"""
输出:
大:  30.0
小:  -50.013
小:  -50.013
大：  30.0
"""
