"""
python获取每个文件的名称和大小.py
http://bbs.bathome.net/thread-39660-1-1.html
2016年3月12日 23:52:29 codegay
"""
import os
import glob
import subprocess
[print(os.path.basename(r),str(os.path.getsize(r))+"我知道你很不爽，你咬我啊") for r in os.listdir(".") if os.path.isfile(r)]

[print(os.path.abspath(r),os.path.getsize(r),"字节") for r in glob.glob("*") if os.path.isfile(r)]

[print(subprocess.getoutput(r"""echo off&for %i in (*.*) do (echo %~nxi %~zi)"""),)]

input()
