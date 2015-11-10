@echo off
for /f "skip=1 tokens=2 delims==" %%A in ('wmic /namespace:\\root\wmi PATH MSAcpi_ThermalZoneTemperature get CurrentTemperature /value') do set /a "HunDegCel=(%%~A*10)-27315"
echo %HunDegCel:~0,-2%.%HunDegCel:~-2% Degrees Celsius


@echo off

for /f "delims== tokens=2" %%a in (
    'wmic /namespace:\\root\wmi PATH MSAcpi_ThermalZoneTemperature get CurrentTemperature /value'
) do (
    set /a degrees_celsius=%%a / 10 - 273
)

echo %degrees_celsius%
pause