"""
python提取文本第一列长度为8的内容
http://www.bathome.net/thread-38181-1-1.html
依山居 21:02 2015/11/17
"""
with open("a.txt") as f:
    txt=f.readlines()
    newtxt=[l.split()[0] for l in txt if (len(l.split()[0])==8)]
    newtxt=[l+"\n" for l in newtxt]
with open("out.txt","w+") as f:
    f.writelines(newtxt)
    
    

