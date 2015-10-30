#python检测文件是否存在并修改注册表

import os
import winreg

f=r"c:\windows\system32\ieframe.dll"
#考虑兼容性的话则从系统变量中取系统路径
f=os.environ.get("SystemRoot")+"\system32\ieframe.dll"
print(f)
key=winreg.CreateKeyEx(winreg.HKEY_CLASSES_ROOT,r"CLSID\{00000000-0000-0000-0000-100000000001}\DefaultIcon")
print(key)
