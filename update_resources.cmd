call cd resources
call forfiles /M *.qrc /C "cmd /c pyrcc4 @file -o @fname_rc.py -py3"
call exit