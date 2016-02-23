"""
python合并当前目录的文件.py
2016年2月23日 23:02:02 codegay
http://www.oschina.net/question/2648254_2152024
"""
import os
#如果看不懂,可搜索一下列表解析的文章看看
#os.listdir 列出当前目录下后缀为.py的文件,迭代读取内容写入result.txt
flist=[r for r in os.listdir(".") if os.path.splitext(r)[-1]==".py"]
with open("result.txt","a+") as save:
    for f in flist:
        txt=open(f,encoding="utf-8").read()
        save.write(txt)
        
