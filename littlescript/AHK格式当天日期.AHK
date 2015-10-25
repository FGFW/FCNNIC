;AHK脚本 练手 
;AHK格式化时间 参考：http://ahkcn.sourceforge.net/docs/commands/FormatTime.htm
;方法1 在我这里运行%A_yy%取不到15这个值。推荐方法2
today = %A_yy%%A_MM%%A_DD%
MsgBox %today%

;方法2 第二个参数留空表示取当前本地时间
FormatTime, today, ,yyMMdd
msgbox %today%