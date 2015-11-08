
#python重复行数合并文件
#题目来源: http://www.bathome.net/viewthread.php?tid=38017
#依山居 4:22 2015/11/8

#相关资料 Python按行读文件：
#http://www.cnblogs.com/xuxn/archive/2011/07/27/read-a-file-with-python.html

#相关资料 Python迭代器和生成器：
#http://python.jobbole.com/81881/

#python3 生成器
#http://t.cn/R2GTPBY

#Python关键字yield的解释
#http://pyzh.readthedocs.org/en/latest/the-python-yield-keyword-explained.html

#探寻Python中如何同时迭代多个iterable对象
#http://blog.csdn.net/kxcfzyk/article/details/41380017

#以下三个函数逐行读取对应文件,n为默认重复次数。
def txta(txta="a.txt",n=6):
    with open(txta) as fa:
        for la in fa:
            la=la.rstrip()+","
            for r in range(n):
                yield la
        
def txtb(txtb="b.txt",n=3):
    with open(txtb) as fb:
        for lb in fb:
            lb=lb.rstrip()+","
            for r in range(n):
                yield lb

def txtc(txt="c.txt",n=1):
    with open(txt) as f:
        for l in f:
            l=l.rstrip()+"\n"
            for r in range(n):
                yield l

def merge(a,b,c,txt="test.txt"):
    with open(txt,"a+") as f:
        f.write(a+b+c)
        #f.flush()
        
bt=txtb()
at=txta()
for c in txtc():
    b=next(bt)
    a=next(at)
    merge(a,b,c)

try:
    input("执行完成,按回车退出")
except SyntaxError:
    pass
