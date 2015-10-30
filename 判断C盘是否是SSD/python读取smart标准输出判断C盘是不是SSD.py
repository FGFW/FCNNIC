#python读取管道判断C盘是不是SSD
#依赖开源工具smartmontool中的ssmartctl.exe
#http://sourceforge.net/projects/smartmontools/

#方法1
import os
txt=os.popen('smartctl -i e:').read()
if 'Solid State Device' in txt:
    print("是SSD\n")
else:
    print("也许大概不是SSD\n")

#方法2    
#少数情况下C盘不是系统盘，从系统系统变量从读取系统盘符可靠性会高一些。
cmd='smartctl -i '
sd=os.environ.get('SYSTEMDRIVE')
print("当前系统盘符:",sd)
cmd=cmd+sd
print('即将要执行的命令：',cmd)
txt=os.popen(cmd).read()
if 'Solid State Device' in txt:
    print("systemdrive:",sd,"固态硬盘")

    
