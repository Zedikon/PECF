@echo off
echo starting building PECF
python setup.py sdist bdist_wheel
echo Building sucess!
pause