@echo off

::�������ж�C���Ƿ���SSD.bat
::������Դ����smartmontool�е�ssmartctl.exe
::http://sourceforge.net/projects/smartmontools/
smartctl -i %systemdrive%|find "Solid State Device"&&echo ������SSD||echo - -����SSD

smartctl -a d: |find "Solid State Device"&&echo ������SSD||echo - -����SSD

smartctl -a e: |find "Solid State Device"&&echo ������SSD||echo - -����SSD

pause