#python生成测试数据
#依山居 10:07 2015/11/11

import random
import string
import time
start=time.time()
az=string.ascii_uppercase

out=open("b.txt","a+")
for r in range(10000000):
    ts=""
    for s in range(1,random.randint(1,10)):
            #razint=random.randint(0,25)
            #raz=az[razint] #-_- random.choice()方法,简单也是等效的。
            raz=random.choice(az)
            rf=random.uniform(-99,999)
            rf=round(rf,random.randint(0,4))
            ts+=raz+str(rf)+" "

    out.write(ts+"\n")
            
out.close()
end=time.time()
pt=end-start

print("程序运行时间：",pt)
try:
    input("按回车退出")
except SyntaxError:
    pass

