@echo off
cd C:\Users\Zedikon\Desktop\PECF
python setup.py sdist bdist_wheel
echo Sucess PECF build! Uploading file's
cd Build
upload.bat
