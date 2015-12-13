"""
文本文件隔行删除或每隔几行删除
http://www.bathome.net/thread-38581-1-1.html
依山居 21:49 2015/12/13
python代码量略大~
"""
with open("1.txt") as f:
    txt=f.readlines()
ln=len(txt)
result=[txt[r-1] for r in range(1,ln+1) if r%2 !=0]
[print(r) for r in result]
with open("result.txt","w+") as f:
    f.writelines(result)

