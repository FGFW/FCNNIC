"""
python字典取出文件倒数第N行.py
http://www.bathome.net/thread-38591-1-1.html
依山居 7:44 2015/12/14
本质还是对数组进行操作
思路是生成行号，倒序历遍文件(因为是倒数行号)，生成字典，行号作为字典键。
这样使用时会方便。
"""
with open("1.txt") as f:
    txt=f.readlines()
keys=[r for r in range(1,len(txt)+1)]
result={k:v for k,v in zip(keys,txt[::-1])}
print(result[2])#取出倒数第二行
print(result[3])#取出倒数第三行
