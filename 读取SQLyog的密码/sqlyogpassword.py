# -*- coding: utf-8 -*-
"""
Created on 2017-03-15 07:42:58

@author: codegay
"""

import os
import configparser
import base64


def decode(base64str):
    tmp = base64.b64decode(base64str)
    return bytearray([(b<<1&255)|(b>>7) for b in tmp]).decode("utf8")

sqlyogini = os.environ.get('APPDATA')+"\\SQLyog\\sqlyog.ini"
print("sqlyogini文件路径:",sqlyogini)
ini = configparser.ConfigParser()
ini.read(sqlyogini,encoding='utf8')

connections = [r for r in ini.sections() if 'name' in ini.options(r) and ini.get(r,'password')]

for c in connections:
    name = ini.get(c,'name')
    host = ini.get(c,'host')
    user = ini.get(c,'user')
    b64pass = ini.get(c,'password')
    password = decode(b64pass)
    print(name,host,user,sep='\n')
    print('密码',password)
    print('----------------------------------------------------------------------------------')
