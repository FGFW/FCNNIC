;ahk取计算机名拼接IP地址

EnvGet, cn, COMPUTERNAME
MsgBox, 计算机名:%cn%
;cn = jumper33 ;测试
fd := RegExMatch(cn, "(\d{1,3})$", s)

msgbox %s%
s +=10
ip = 192.168.1.%s%
msgbox %ip%