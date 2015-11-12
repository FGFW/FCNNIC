"""
一列文本进行字符串格式操作转成三列2
依山居 8:18 2015/11/12

相关资料: 飘逸的python - 增强的格式化字符串format函数
http://blog.csdn.net/handsomekang/article/details/9183303

总结，我自己生成了百万行来测试，文本文件8M大，内容为1-999999
这里的代码完成处理需要85秒左右，比如前面的代码快了五十秒左右。

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
    print("运行耗时1：",pt) #运行耗时： 0.08600497245788574
    
    l=txt.rsplit()
    
    end=time.time()
    pt=end-start
    print("运行耗时2：",pt)
    
    l=l+(3-len(l)%3)*[" "]

    end=time.time()
    pt=end-start
    print("运行耗时3：",pt) #运行耗时： 0.22101211547851562
#=======================================
    #测试发现这个阶段耗费了绝大部分时间
    while l:
        #字符串格式化,两个格式化方法都可以
        #ft="%s  %s  %s\n" % (l[0],l[1],l[2])
        ft='{0}  {1}  {2}\n'.format(l[0],l[1],l[2])
        nl.append(ft)
        del(l[0:3])
        
end=time.time()
pt=end-start
print("运行耗时4：",pt) #运行耗时： 82.27809810638428
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

