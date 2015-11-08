@echo off
::注释区
goto :code
依山居 1:54 2015/11/9

fr修改WallpaperType.bat
http://www.bathome.net/thread-38056-1-1.html

fr是一个完整支持正则表达式查找替换的命令行工具，
作者网站：http://baiy.cn/utils/fr/index.htm

去掉-stdout参数则直接修改原文件

:code
::直接修改原文件
fr -r:"\"WallpaperType\":\d+," -t:"\"WallpaperType\":0," -trc x.json


::修改的内容，原文件不修改,重定向输出到新文件。
fr -r:"\"WallpaperType\":\d+," -t:"\"WallpaperType\":0," -stdout -trc x.json>test.txt

pause
