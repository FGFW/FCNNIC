"""
13:05 2015/11/30

"""

import winreg
import re

reg=winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER,r"Software\Blizzard Entertainment\Warcraft III\String")
id=winreg.QueryValueEx(reg,"userlocal")

rs=re.fullmatch(r"[\w]+",id[0])
rs.group()

print(rs)

print(id)
"""
try:
    reg=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Blizzard Entertainment\Warcraft III\String")
    id=winreg.QueryValue(reg,"userlocal")
    print(id)
    
except FileNotFoundError:
    print("魔兽争霸注册表不存在，可能是未安装魔兽争霸或者没有导入注册表")
    

"""
