"""
python把不以引号结尾的行与下一行连接
题目来源 http://www.bathome.net/thread-38164-1-1.html
依山居  13:13 2015/11/17
就是当是练习列表解析用法了
"""
newtxt=[]
with open("a.txt") as f:
    txt=f.readlines()
    txt=[r.rstrip() for r in txt]
    rn=len(txt)
    print("总行数:",rn)
    newtxt=[txt[r][:]+txt[r+1][:] if ('\"' not in txt[r][-1]) else txt[r] for r in range(rn) ]
    newtxt=[r+"\n" for r in newtxt if '\"' in r[0]]
    f.close()
    
with open("b.txt","w+") as f:
    f.writelines(newtxt)
    f.close()
