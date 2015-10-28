@echo off

::批处理判断C盘是否是SSD.bat
::依赖开源工具smartmontool中的ssmartctl.exe
::http://sourceforge.net/projects/smartmontools/
smartctl -i %systemdrive%|find "Solid State Device"&&echo 看来是SSD||echo - -不是SSD

smartctl -a d: |find "Solid State Device"&&echo 看来是SSD||echo - -不是SSD

smartctl -a e: |find "Solid State Device"&&echo 看来是SSD||echo - -不是SSD

pause