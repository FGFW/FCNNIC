import winreg
x=r"Applications\javaw.exe\shell\open\command"

r=winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,r"Applications\javaw.exe")

