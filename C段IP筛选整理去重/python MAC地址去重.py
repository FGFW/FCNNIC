"""
python MAC地址去重.py
http://bbs.bathome.net/thread-39529-1-1.html
2016年3月1日 19:46:32 codegay
"""
#不保持mac行的顺序
txt=open("mac.bat").readlines()
re=list(set(txt[1:-2]))+txt[-2:]
open('mac_new.bat',"w+").writelines(re)
