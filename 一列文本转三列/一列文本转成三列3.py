"""
一列文本进行字符串格式操作转成三列3
依山居 8:18 2015/11/12
题目来源 http://www.bathome.net/thread-38097-1-1.html
相关资料: 飘逸的python - 增强的格式化字符串format函数
http://blog.csdn.net/handsomekang/article/details/9183303

总结，我自己生成了百万行来测试，文本文件8M大，内容为1-999999
吐槽，改成列表解析百万行数据一秒能处理完，之前写的程序没法看了....
"""
print("运行中..."*3)
import time
start=time.time()

l=[]
nl=[]
ft=''
out=open("out.txt","w+")
with open("a.txt") as f:
    txt=f.read()
    
    end=time.time()
    pt=end-start
    print("运行耗时1：",pt) 
    
    l=txt.rsplit()
    
    end=time.time()
    pt=end-start
    print("运行耗时2：",pt)
    d=[0,2,1]
    m=len(l)%3
    print(len(l),len(l)%3)
    
    l=l+(d[m])*["--"]
    print(len(l),len(l)%3)
    end=time.time()
    pt=end-start
    print("运行耗时3：",pt) 
#=======================================
    
nl=["%s  %s  %s\n" % (l[r],l[r+1],l[r+2]) for r in range(0,len(l),3)]

end=time.time()
pt=end-start
print("运行耗时4：",pt) 
#=======================================
out.writelines(nl)
out.close()

end=time.time()
pt=end-start
print("运行耗时：",pt)
try:
    input("按回车退出")
except SyntaxError:
    pass

