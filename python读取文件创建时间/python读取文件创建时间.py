"""
python读取文件创建时间修改时间.py
http://www.oschina.net/code/snippet_191887_54050
2016年2月26日 02:55:20 codegay
windows python读取文件的修改时间，创建时间，访问时间信息
需要自己使用time模块进行转换处理
"""
import os
import time

for r in os.listdir("."):
    if r.endswith(".py"):
        t=os.stat(r)
        print(t)
        print("修改时间:",t.st_mtime)
        print(time.localtime(t.st_mtime))
        print("创建时间?",time.localtime(t.st_ctime))
        print("访问时间：",time.ctime(t.st_atime))

#读取目录的时间        
t=os.stat("c:/windows")
print(t)
print("修改时间:",t.st_mtime)
print(time.localtime(t.st_mtime))
print("创建时间?",time.localtime(t.st_ctime))
print("访问时间：",time.ctime(t.st_atime))
