import shutil as s
import os

pwd = os.getcwd()
floder = os.listdir(pwd)
floder.remove('test_7_movefile.py')

for i in floder:
    os.chdir(i)
    for f in os.listdir('.'):
        s.move('.', pwd)
    os.chdir(pwd)