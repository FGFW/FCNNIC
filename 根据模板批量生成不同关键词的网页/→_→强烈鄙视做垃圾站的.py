# -*- coding: utf-8 -*-
#→_→强烈鄙视做垃圾站的
import codecs
ohost=open("host.txt","r")
host=ohost.readlines()
ohost.close()
okey=open("key.txt")
if okey[:3] == codecs.BOM_UTF8:
    okey = okey[3:]
print (okey.decode("utf-8"))
key=okey.readline()
for k in key():
    
    print(key)
okey.close()
omoban=open("moban.htm","r")
moban=omoban.read()
omoban.close()
