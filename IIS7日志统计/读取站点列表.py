"""
python正则读取IIS7配置文件
依山居 2016年2月1日 07:50:46
"""
import os
import re

#IIS 7-8的配置文件路径是 %windir%\system32\inetstr\config\applicationHost.config
#WMI读取信息非常慢，直接读配置文件的话，当然会非常快。

env=os.environ['windir']+r"\System32\inetsrv\config\applicationHost.config"
#evn="C:\windows\system32\inetsrv\config\applicationHost.config"

xml=open(env).read()

sites=re.findall(r'''<site name="(.+)" id="(\d+)".+physicalPath="(.*?)"''',xml,re.S)
logpath=re.findall(r'<siteDefaults>.+directory="(.+?)" />',xml,re.S)
print(sites)
print(logpath)
input("")
