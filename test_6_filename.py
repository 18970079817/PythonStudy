import os

pwd = os.getcwd()
floder = os.listdir(pwd)
floder.remove('test_6_filename.py')

for i in floder:
    os.chdir(i)
    for f in os.listdir('.'):
        new_name = i.split('_')[-1] + '_' + f
        os.rename(f, new_name)
    os.chdir(pwd)
