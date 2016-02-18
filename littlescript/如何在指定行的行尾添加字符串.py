"""
如何在指定行的行尾添加字符串.py
http://bbs.bathome.net/thread-39409-1-1.html
2016年2月18日 15:39:44 codegay
python
"""
with open("a.txt","r+") as f:
    txt=f.readlines()
    txt[2]=txt[2].rstrip("\n")+";\n"
    f.seek(0)
    f.writelines(txt)
