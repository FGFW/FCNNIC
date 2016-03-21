"""
python socket发送魔法包网络唤醒开机.py
2016年3月20日 20:40:42 codegay

_(:3」∠)_愿佛祖保佑我主永无BUG→_→

参考不止以下文章,不能一一列出,均在此表示感谢:

一个简单的python socket编程:
http://openexperience.iteye.com/blog/145701

wireshark维基百科 WakeOnLAN (WOL):
https://wiki.wireshark.org/WakeOnLAN

python wakeonlan库
https://github.com/remcohaszing/pywakeonlan

#WOL支持4-6位的密码 WOL数据包格式'FF'*6+MAC地址重复16次+密码
"""
import socket
import pprint
import binascii
"""mac.txt的格式化为每行一个mac地址.如下任意形式的mac地址:
FFFFFFFFFFFF
44850004F4EE
00-FF-AC-C0-BB-CA
44-85-00-04-F4-EE
44:87:01:04:F4:EE
"""
f=lambda x:x.strip() if len(x.strip())==12 else x.strip().replace(x.strip()[2],"")
mac=[f(r) for r in open("mac.txt")]
print("目标MAC地址列表:")#mac.txt中的mac地址会被处理成FFFFFFFFFFFF无分隔符紧揍形式
pprint.pprint(mac)
ip="192.168.199.255"
port=9
ps="fsfafda" #password 
ps=ps.encode()

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
def sendto(r):
    s.sendto(r,(ip,port))

#python利用or在列表解析中调用多个函数 http://www.cnblogs.com/gayhub/p/5277919.html
[print("正在向:",r,"施法!") or sendto(binascii.unhexlify('FF'*6+r*16)+ps) for r in mac]
s.close()
input("打完收功,回车退出!")
#2016年3月21日 19:54:36
