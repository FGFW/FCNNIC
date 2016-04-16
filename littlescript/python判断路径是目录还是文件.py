"""
python判断路径是目录还是文件.py
http://bbs.bathome.net/thread-39957-1-1.html
2016年4月8日 03:04:00 codegay
"""


import os

files=[r for r in open("test.txt") if os.path.isfile(r.strip())]
dirs=[r for r in open("test.txt") if os.path.isdir(r.strip())]

with open("11.txt","w+") as f:
    f.writelines(files)

with open("22.txt","w+") as f:
    f.writelines(dirs)
