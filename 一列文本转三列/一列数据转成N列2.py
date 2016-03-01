"""
一列数字转成N列2.py
http://www.oschina.net/question/2400361_2152116
2016年3月1日 23:49:33 codegay
这个问题本质等于问如何把一个列表或者一个字符串分成N份
参考http://blog.topspeedsnail.com/archives/1469
"""
#生成测试数据,得到a.txt为1列1-999的内容
with open("a.txt","w+") as f:
    [f.write(str(r).zfill(4)+"\n") for r in range(1,999)]

#一列数字转成N列.py
N=50
txt=[r.rstrip("\n") for r in open("a.txt").readlines()]
re=[txt[r:r+N] for r in range(0,len(txt),N)]
f=open("out.txt","w+")
[f.write(','.join(r)+"\n") for r in re]    
f.close()
