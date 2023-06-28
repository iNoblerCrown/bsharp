set current_directory=%~dp0
cd C:\
md bsharp
set x = "main.py"
set z = "C:\bsharp"
cd %current_directory%
move %x% "%z%\"
set x = "bs.bat"
move %x% "%z%\"
set x = "bsharp.bat"
move %x% "%z%\"
set y= "Write 'finish' to finish the installation."
echo %y%
