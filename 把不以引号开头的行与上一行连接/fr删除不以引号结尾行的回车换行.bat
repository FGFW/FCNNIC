@echo off
::22:14 2015/11/16

fr a.txt -ric:(\"[0-9,a-z]+)\r\n -t:"\1" -stdout

pause