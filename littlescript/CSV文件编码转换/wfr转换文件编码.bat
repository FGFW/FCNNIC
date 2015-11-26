@echo off
goto code
注释区
wfr转换CSV文件编码.bat
依山居 18:45 2015/11/26
wfr 下载及中文说明: http://baiy.cn/utils/wfr/index.htm
题目来源: http://www.bathome.net/thread-26023-1-1.html

:code
copy text.csv test.csv /y
wfr test.csv -f:"?" -t:"¶" -encarg:utf-8 -encin:gbk -encout:utf-8 
pause