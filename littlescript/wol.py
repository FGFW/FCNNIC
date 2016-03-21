"""
python socket发送魔法包网络唤醒开机.py
2016年3月20日 20:40:42 codegay
参考以下文章,在此表示感谢:

一个简单的python socket编程:
http://openexperience.iteye.com/blog/145701

wireshark维基百科 WakeOnLAN (WOL):
https://wiki.wireshark.org/WakeOnLAN
"""

import socket
import struct
"""mac.txt的格式化为每行一个mac地址.如下任意形式的mac地址:
FFFFFFFFFFFF
44850004F4EE
00-FF-AC-C0-BB-CA
44-85-00-04-F4-EE
44:87:01:04:F4:EE
"""

f=lambda x:x.strip() if len(x.strip())==12 else x.strip().replace(x.strip()[2],"")
mac=[f(r) for r in open("mac.txt")]
print("目标MAC地址列表:",mac)#mac.txt的地址会被处理成FFFFFFFFFFFF的形式

ip="255.255.255.255"
port=9
host=(ip,port)

data=[('FF'*6+r*17).encode() for r in mac]
print(data)

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
s.connect(host)

