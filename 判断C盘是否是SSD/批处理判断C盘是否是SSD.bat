#�������ж�C���Ƿ���SSD.bat
#������Դ����smartmontool�е�ssmartctl.exe

smartctl -i %systemdrive%|find "Solid State Device"&&echo ������SSD

smartctl -a d: |find "Solid State Device"&&echo ������SSD

