@echo off

echo Drive type identification using LogicalDisk/DriveType=3:
for /F "tokens=1-2" %%a in ('wmic LogicalDisk get DeviceID^,DriveType') do (
   if "%%b" equ "3" (
      echo Drive %%a is a HDD
   )
)

echo/
echo Drive type identification using DiskDrive/InterfaceType=IDE:
set partitions=0
for /F "tokens=1-2" %%a in ('wmic DiskDrive get InterfaceType^,Partitions') do (
   if "%%a" equ "IDE" set /A partitions+=%%b
)
set drives=BCDEFGHIJKLMNOPQRSTUVWXYZ
call set lastIDEdrive=%%drives:~%partitions%,1%%:
echo Last IDE interface logical drive (B:=none): %lastIDEdrive%
for /F %%a in ('wmic LogicalDisk get DeviceID') do (
   if "%%a" gtr "%lastIDEdrive%" (
      echo Drive %%a is NOT a HDD
   )
)

PAUSE