echo.
echo 
echo.
fastboot -s HT4CHSF01311 getvar cid

fastboot -s HT4CHSF01311 -s HT4CHSF01311 erase cache

fastboot -s HT4CHSF01311 oem erase_phone_storage

fastboot -s HT4CHSF01311 oem readcid

fastboot -s HT4CHSF01311 oem rebootRUU

ping 127.0.0.1 -n 15>nul 

fastboot -s HT4CHSF01311 flash zip rom.zip

fastboot -s HT4CHSF01311 reboot

echo.
ping 127.0.0.1 -n 15>nul 


exit
