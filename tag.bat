@echo off

echo tworzenie taga
set /p tag_ver= "Wersja texturpacka (1.0, 2.0, itd.): "
git tag v%tag_ver%
git push --tags
pause