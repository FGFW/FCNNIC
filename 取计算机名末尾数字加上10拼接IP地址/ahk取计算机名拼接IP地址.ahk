;ahkȡ�������ƴ��IP��ַ

EnvGet, cn, COMPUTERNAME
MsgBox, �������:%cn%
;cn = jumper33 ;����
fd := RegExMatch(cn, "(\d{1,3})$", s)

msgbox %s%
s +=10
ip = 192.168.1.%s%
msgbox %ip%