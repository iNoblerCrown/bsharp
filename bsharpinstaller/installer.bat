set current_directory=%~dp0
cd C:\
md bsharp
cd %current_directory%
move "bs.bat" "C:\bsharp"
move "bsharp.bat" "C:\bsharp"
move "main.py" "C:\bsharp"
cd C:\bsharp
cmd /k
set y= "Installation finished."
echo %y%
del "%~f0"