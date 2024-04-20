@echo off

echo dodawanie plikow
git add .

set /p c_message= "Co dodales (krotko): "
git commit -m "%c_message%"

git push origin main
pause