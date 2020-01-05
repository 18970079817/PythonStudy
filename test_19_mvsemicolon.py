import os
import os.path
import shutil

pathDir = 'F:\\Data\\OtherTxt\\'
os.chdir(pathDir)
files = os.listdir(pathDir)
for f in files:
    print f
    with open(f, 'r') as g:
        firstline = g.readline()
        if len(firstline.split(';')) == 2:
            pass
        else:
            shutil.copy(f, 'F:\\Data\\UserPassTxt\\movesemicolon\\')
