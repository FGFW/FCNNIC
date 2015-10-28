#python 判断C盘是不是SSD
#依赖pySMART模块以及开源工具smartmontool中的ssmartctl.exe
#https://github.com/jakogut/pySMART
#http://sourceforge.net/projects/smartmontools/

import pySMART

os=pySMART.utils
#devlist=pySMART.DeviceList()
#devlist.devices[0]
dev=pySMART.Device("pd1")
print(dev)

x=os.rescan_device_busses()

