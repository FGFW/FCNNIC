"""
python切片提取一组数据的第一个字符以及第一个到第三个字符.py
http://www.bathome.net/thread-38635-1-1.html
依山居 1:02 2015/12/17
"""
with open("data.txt") as f:
    txt=[r.rstrip().split() for r in f.readlines()]
    
result1=''
result2=''
for r in txt:
    sstr1=''
    sstr2=''
    for s in r:
        if len(s)>3:
            sstr1+=s[0]+" "
            sstr2+=s[0:3]+" "
        else:
            sstr1+=s
            sstr2+=s
    result1+=sstr1+"\n"
    result2+=sstr2+"\n"

with open("result1.txt","w+") as f:
    f.write(result1)
with open("result2.txt","w+") as f:
    f.write(result2)
