"""
生成测试数据
http://bbs.bathome.net/thread-38881-1-1.html
依山居 2016年1月4日 09:42:40
"""

#生成测试数据
txt=[str(r).ljust(7,"@")+"\n" for r in range(1,10000)]
with open("数据.txt","w+") as f:
    f.writelines(txt)

#生成0000-9999序列待用
sq=[str(r).zfill(4)+"\n" for r in range(0,10000)]
with open("序列.txt","w+") as f:
    f.writelines(sq)
