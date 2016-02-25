"""
python正则提取分子信息sdf文件内容.py
http://www.oschina.net/question/2650430_2152434
2016年2月25日 04:17:05 codegay
python 3.4
"""
import sys
import re
print(sys.argv)
if len(sys.argv)>=4:    
    sdffile=sys.argv[1]
    inputfile=sys.argv[2]
    result=sys.argv[3]
elif len(sys.argv)==1:
    sdffile="exemple.sdf"
    inputfile="exemple_data.csv"
    result="result.txt"
    
sdf=open(sdffile).read()
#print(sdf)
inlist=[r.strip("\n") for r in open(inputfile).readlines()]
#print(inlist)
with open(result,"a+") as f:
    for i in inlist:
        out=re.findall(r"%s.*?\$\$\$\$" %i,sdf,16)
        print(out)
        [f.write(r) for r in out]
    
