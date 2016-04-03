"""
python文件名插入指定行.py
http://bbs.bathome.net/thread-39833-1-1.html
2016年4月3日 13:08:57 codegay
"""
fn="temp.txt"
with open(fn) as f:
    txt=f.readlines()
    txt.insert(3,fn+"\n")#文件名加上换行符号插入第四行

with open(fn,"w+") as f:
    f.writelines(txt)
