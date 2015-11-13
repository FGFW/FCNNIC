"""
生成测试数据
依山居 19:46 2015/11/13
python列表解析真好玩~
"""
import time
start=time.time()

an=1
bn=2
cn=6
x=1000000
al=["%012d\n" % r for r in range(an*x)]
bl=["%012d\n" % r for r in range(bn*x)]
end=time.time()
pt=end-start
print("运行耗时1：",pt)
cl=["%012d\n" % r for r in range(cn*x)]
end=time.time()
pt=end-start
print("运行耗时2：",pt)

atxt=open("aa.txt","w+")
atxt.writelines(al)
atxt.close()

btxt=open("bb.txt","w+")
btxt.writelines(bl)
btxt.close()

end=time.time()
pt=end-start
print("运行耗时3：",pt)

ctxt=open("cc.txt","w+")
ctxt.writelines(cl)
ctxt.close()

end=time.time()
pt=end-start
print("运行耗时：",pt)

try:
    input("按回车退出")
except SyntaxError:
    pass
