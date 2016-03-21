"""
python wakeonlan实现电脑网络开机.py
http://bbs.bathome.net/thread-39732-1-1.html

2016年3月20日 13:03:16 codegay

https://pypi.python.org/pypi/wakeonlan/0.2.2
pip命令安装模块
pip install wakeonlan

把mac地址收集后,一行一个存在mac.txt中.
使用Wireshark抓了下包,发现多网卡的环境下是使用其中的一个网卡发送的.
广播包可能发不到指定的网段里,所以需要指定一下目标网段的IP.
"""
from wakeonlan import wol

with open("mac.txt") as f:
    for mac in f:
        wol.send_magic_packet(mac.strip(),ip_address="192.168.199.255")
