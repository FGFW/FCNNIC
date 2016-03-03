"""
python取出当前目录下最新修改的文件.py
http://bbs.bathome.net/thread-39535-1-1.html
2016年3月2日 11:44:35 codegay
参考资料 python glob模块 通配符
http://blog.sina.com.cn/s/blog_5ee725480101bf94.html
"""
import os
import glob
import shutil
#os.mkdir("电路图")
fs=glob.glob("*总成电路图.pdf")
电路图={r:os.stat(r).st_mtime for r in fs}
ns=max(电路图)
print(ns)
print("最新",max(电路图))
print(ns)
shutil.copy(ns,"./电路图/")

fs=glob.glob("*总成明细表.pdf")
明细表={r:os.stat(r).st_mtime for r in fs}
print("最新",max(明细表))
