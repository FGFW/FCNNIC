"""
python wakeonlan实现电脑网络开机.py
http://bbs.bathome.net/thread-39732-1-1.html

2016年3月20日 13:03:16 codegay

https://pypi.python.org/pypi/wakeonlan/0.2.2
pip命令安装模块
pip install wakeonlan

把mac地址收集后,一行一个存在mac.txt中

"""
from wakeonlan import wol

with open("mac.txt") as f:
    for mac in f:
        wol.send_magic_packet(mac.strip())

        
        
        
    
