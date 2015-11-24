"""
python截取文件指定行进行合并.py
http://bbs.bathome.net/thread-38205-1-1.html
依山居 23:10 2015/11/24
懒得解释~
"""
import re
import os
import sys

datadirs="./DATAS/"
outputdirs="./DATAS/合并后/"

ls=os.listdir(datadirs)
rec=re.compile(r"([A-Z]{2}-[A-Z]\d-[A-Z]\d)-\d{2}.csv")
fn={r for r in re.findall(rec,str(ls))}
fn=sorted(fn)

if len(fn)<1:
    input("没有找到文件")
    sys.exit(0)

for r in fn:
    csv1=datadirs+r+"-01.csv"
    csv2=datadirs+r+"-02.csv"
    csv3=datadirs+r+"-03.csv"
    out=r+".csv"

    if os.path.exists(csv1):
        with open(csv1) as f:
            c1=f.readlines()[:3]
    if os.path.exists(csv2):
        with open(csv2) as f:
            c2=f.readlines()[3:]
        c1=c1+c2
    if os.path.exists(csv3):
        with open(csv3) as f:
            c3=f.readlines()[3:]
        c1=c1+c3
    with open(outputdirs+out,"w+") as f:
        f.writelines(c1)

        
        
        
            
        
