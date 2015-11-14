"""

"""

import time
start=time.time()

an=6
with open("aa.txt") as f:
    ta=f.read()
    ta=ta.rsplit()
    al=[(r+",") for r in ta]*an
    al=sorted(al)
print(len(al))   
bn=3
with open("bb.txt") as f:
    tb=f.read()
    tb=tb.rsplit()
    bl=[(r+",") for r in tb]*bn
    bl=sorted(bl)
    
print(len(bl))    
cn=1
with open("cc.txt") as f:
    tc=f.read()
    tc=tc.rsplit()
    cl=[r+"\n" for r in tc]
print(len(cl))
end=time.time()
pt=end-start
print("运行耗时：",pt)

rn=len(cl)
tal=[]
for r in range(rn):
    tal.append(al[r]+bl[r]+cl[r])
    
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
