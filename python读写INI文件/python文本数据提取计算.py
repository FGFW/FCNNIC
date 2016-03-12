"""
python文本数据提取计算.py
http://bbs.bathome.net/thread-39649-1-1.html
codegay 2016年3月12日 12:19:56

"""
import random
import re
import shutil
#测试数据
shutil.copy("test.txt","a.txt")

outf=open("b.txt","w+",encoding="utf-8")
t=lambda x,y:y.write(x) if "Exp =" not in x else y.write(x.split("=")[0]+" = "+str(int(x.split("=")[1].strip())//4)+"\n")


#读取数据,懒得写正则了，假设数据格式严格：exp= 数值
with open("a.txt",encoding="utf-8") as f:
    txt=[t(r,outf) for r in f.readlines()]
outf.close()

#设置a为源文件,处理过的数据临时写入b,程序结束后，复制b覆盖a
shutil.copy("b.txt","a.txt")
#2016年3月12日 12:50:13
