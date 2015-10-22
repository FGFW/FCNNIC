根据获取的注册表中指定的值修改注册表某个字符串中个别字符

举例：
     先获取到注册表：\HKEY_CLASSES_ROOT\Applications\javaw.exe\shell\open\command 下的默认值（只有一个键值，若没有这个找到这个路劲则创建，如下说明）
            若没有找到这个路劲则创建这个路劲然后，在这个command文件夹下创建一个键值，键名字默认，值为：D:\Program Files (x86)\Java\jdk1.6.0_33\jre\bin\javaw.exe" -jar "%1" %
            若存在则取到这个(默认)键对应的值 "D:\Program Files (x86)\Java\jdk1.6.0_33\jre\bin\javaw.exe" "%1" %"
            判断上面的取到的值中是否包含jar这个字符串，若不包含jar字符串那么久修改那个值 D:\Program Files (x86)\Java\jdk1.6.0_33\jre\bin\javaw.exe" -jar "%1" %