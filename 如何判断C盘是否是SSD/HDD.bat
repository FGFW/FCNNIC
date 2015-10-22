@echo off

for /F "tokens=1-4" %%a in ('wmic logicaldisk get Description^,DeviceID') do (
   if "%%a %%b %%c" equ "Local Fixed Disk" (
      echo Drive %%d is a HDD
   )
)

pause