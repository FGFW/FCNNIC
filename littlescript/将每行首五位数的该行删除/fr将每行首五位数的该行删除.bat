@echo off
::依山居 5:51 2015/11/8

::fr将每行首五位数的该行删除 
::http://www.bathome.net/thread-38036-1-1.html

::fr是一个完整支持正则表达式查找替换的命令行工具，
::作者网站：http://baiy.cn/utils/fr/index.htm

::去掉-stdout参数则直接修改原文件


fr -r:"^\d{5},.*\r?\n?" -t -stdout -trc a.txt

pause