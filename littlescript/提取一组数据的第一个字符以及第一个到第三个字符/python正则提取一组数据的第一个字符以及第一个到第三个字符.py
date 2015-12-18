"""
python正则提取一组数据的第一个字符以及第一个到第三个字符
http://www.bathome.net/thread-38635-1-1.html
 依山居 3:43 2015/12/19

"""
import re
with open("data.txt") as f:
    txt=f.read()
    
rep=re.compile("(\w|~{1})(\w*)")
result1=re.sub(rep,"\\1",txt)
with open("result1.txt","w+") as f:
    f.write(result1)

rep=re.compile("(\w{3})(\w*)")
result2=rep.sub("\\1",txt)
with open("result2.txt","w+") as f:
    f.write(result2)

        
