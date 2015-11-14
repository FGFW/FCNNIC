"""
每行数据重复N次合并生成新文件
题目来源 http://www.bathome.net/thread-38017-2-1.html
依山居 0:54 2015/11/14
这个版本可以使用来处理实际数据。。。6百万行，大约17秒。。。
总结：几百万行数据真不算多。不需要逐行读取处理。python列表解析是个好东西~

使用重复列表中元素更好的方法 http://www.oschina.net/question/96078_2141454
python笔记_列表解析 http://www.jianshu.com/p/c635d3c798c2
"""

import time
start=time.time()

an=6
with open("aa.txt") as f:
    ta=f.read()
    ta=ta.rsplit()
    al=[r+"," for r in ta for i in range(an)]
print("al长度:",len(al))

bn=3
with open("bb.txt") as f:
    tb=f.read()
    tb=tb.rsplit()
    bl=[r+"," for r in tb for i in range(bn)]
print("bl长度:",len(bl))

cn=1
with open("cc.txt") as f:
    tc=f.read()
    tc=tc.rsplit()
    cl=[r+"\n" for r in tc for i in range(cn)]
print("cl长度:",len(cl))

end=time.time()
pt=end-start
print("运行耗时：",pt)

rn=len(cl)
tal=[al[r]+bl[r]+cl[r] for r in range(rn)]
#还是用列表解析好~
#for r in range(rn):
#   tal.append(al[r]+bl[r]+cl[r])
    
end=time.time()
pt=end-start
print("运行耗时：",pt)

with open("out.txt","w+") as f:
    f.writelines(tal)
    f.close()
    
end=time.time()
pt=end-start
print("运行耗时：",pt)
try:
    input("按回车退出")
except SyntaxError:
    pass
