@echo off
(for /f "tokens=1* delims=:" %%a in (a.txt) do (
    for %%c in (%%b) do echo %%a：%%c
))>b.txt