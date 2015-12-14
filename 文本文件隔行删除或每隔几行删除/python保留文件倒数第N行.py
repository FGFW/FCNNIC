"""
http://www.bathome.net/thread-38591-1-1.html
保留文件倒数第N行
依山居 6:08 2015/12/14
这个问题本质还是可以看是操作列表元素
"""
with open("1.txt") as f:
    txt=f.readlines()
ln=len(txt)
result=[txt[r] for r in range(ln,0,-1) if r==2 or r==5 or r==8 or r==11]
print(result)
