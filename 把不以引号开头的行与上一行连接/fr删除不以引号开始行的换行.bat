@echo off
::依山居 13:01 2015/11/18
::fr 不带-stdout参数会直接修改原文件，所以复制s.txt为ss.txt运行测试
::fr 使用-s 可以列举子目录修改匹配的文件。注意做好备份
copy a.txt ss.txt /y
::以引号结尾，不以引号开头，就删掉换行。这个规则好处理测试可行。

fr ss.txt -rnnl:\"?(\r?\n+)[^\"] -t:
::type ss.txt

pause