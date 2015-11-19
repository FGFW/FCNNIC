goto code
::注释区
替换文本中的行首年份
fr 下载方法同sed
或者安装batch-cn 输入bcn gt fr可以完成下载
http://baiy.cn/utils/fr/index.htm

:code
copy a1.txt aa1.txt /y

::fr aa1.txt -r:(^2015)(/\d+/\d+) -t:"2013\2"
::fr aa1.txt -r:(^2014)(/\d+/\d+) -t:"2012\2"

::使用^限定替换行首的年份
fr aa1.txt -r:^2015 -t:2013
fr aa1.txt -r:^2014 -t:2012

pause
