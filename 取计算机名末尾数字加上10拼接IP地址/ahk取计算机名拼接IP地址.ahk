;ahkȡ�������ƴ��IP��ַ

EnvGet, cn, COMPUTERNAME
MsgBox, �������:%cn%

fd := RegExMatch(cn, "(\d{1,3})$", s)

msgbox %s%
ip = 192.168.1.%s%
msgbox %ip%