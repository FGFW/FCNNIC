"""
生成测试数据
依山居 20:01 2015/11/24
"""
import time
start=time.time()
print("运行中..."*3)

a=""""1","1
2","123","","201
5-10-31",
"1","1
2","12
3","","",
"1","12","123","123
4"
"A","AB","ABC","ABCD"
"R","RS","RS
T","RSTU"
"E","EF","EFG","EFGH"
"c","EF","EFG","EFGH"
"d","EF","EFG","EFGH
xxx"
"f","EF","EFG","EFGH
13:05 2015/11/17"
"c","EF","EFG","EFGH"
"c","EF","EFG","EFGH"
"c","EF","EFG","EFGH"
"c","EF","EFG","EFGH"
"""

b=a*200000
with open("a.txt","w") as f:
    f.write(b)

end=time.time()
pt=end-start
print("运行耗时：",pt)
try:
    input("按回车退出")
except SyntaxError:
    pass
