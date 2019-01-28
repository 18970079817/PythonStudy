import shutil as s
import os
#move files to the parent folder
pwd = os.getcwd()
floder = os.listdir(pwd)
floder.remove('test_7_movefile.py')

for i in floder:
    os.chdir(i)
    for f in os.listdir('.'):
        oldpath = os.path.abspath(f)
        newpath = os.path.abspath(os.path.join(os.getcwd(), '..'))
        newpath = os.path.join(newpath, f)
        s.move(oldpath, newpath)
    os.chdir(pwd)
