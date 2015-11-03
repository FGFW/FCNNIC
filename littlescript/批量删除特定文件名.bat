@echo off
title 批量删除特定文件名
::by 依山居 9:28 2015/11/3

:: 现在欲删除文本名称中“值”字前面为3位数的文本（比如上列中的 wj3苏州-114值-记录期），也即倒数第9个字符是"_"的文本。这样的代码如何写？
:: http://www.bathome.net/thread-37925-1-1.html

:: everything 的命令行工具es 搜索文件很好用。
:: http://www.bathome.net/thread-37744-1-1.html

::生成测试用的空文件
echo;>wj1苏州-64值-记录期.txt
echo;>wj3苏州-114值-记录期.txt
echo;>wj12苏州-86值-记录期.txt


echo es 搜索文件用法,开启正则的时候\是转义符,所是双斜杠\\
es -r "D:\\temp\\stringtie\\.*-[0-9]{3}值-记录期\.txt"

echo ==============
echo.
echo 可以只搜索文件名,可以搜索到硬盘上文件名匹配的文件
es -r ".*-[0-9]{3}值-记录期\.txt$


echo ==============
echo.
echo 以下是放在for 中执行

for /f "tokens=*" %%a in ('es -r -p "D:\\temp\\stringtie\\.*-[0-9]{3}值-记录期\.txt"') do (
	echo 要删除%%a
	echo del %%a 只是测试用，自行修改删除命令
	)

pause