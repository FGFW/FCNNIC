"""
一列文本转成三列
依山居 16:44 2015/11/11

题目来源 http://www.bathome.net/thread-38097-1-1.html
"""
print("运行中..."*3)
import time
start=time.time()
l=[]
out=open("out.txt","w+")
with open("a.txt") as f:
    txt=f.read()
    l=txt.rsplit()
    #print(l)
    #print(len(l))
    #计算长度，求余，尾部分不够三列的补空位。
    l=l+(3-len(l)%3)*["  "]
    #print(len(l))
    while l:
        #经测试前十万行数据一秒内就能完成。
        #数据量越大，字符串太长的不应该使用下面的写法。
        out.write(l[0]+"  "+l[1]+"  "+l[2]+"\n")
        del(l[0:3])

out.close()

end=time.time()
pt=end-start
print("运行耗时：",pt)
try:
    input("按回车退出")
except SyntaxError:
    pass

