del /F /s /q build\*.*
rmdir /s /q build
del /s /q dist\*.*
.\venv\Scripts\python setup.py sdist bdist_wheel > logs\3.7-64_build.log 2>&1