import os
import os.path
import shutil
#Given a path, move all the user:password txt to a specified dir.

def eachTxtFile(filepath):
    pathDir = os.listdir(filepath)
    num = 0
    for s in pathDir:
        newDir=os.path.join(filepath, s)
        if os.path.isfile(newDir):
            if os.path.splitext(newDir)[1]==".txt":
                num += 1
                print newDir
                with open(newDir, 'r') as f:
                    firstline = f.readline()
                    if len(firstline.split(':')) == 2:
                        dst = 'F:\\Data\\UserPassTxt\\'
                        dst = dst + (newDir.split('\\')[-1]) + (str(num))
                        shutil.copy(newDir, dst)
                    else:
                        dst = 'F:\\Data\\OtherTxt\\'
                        dst = dst + (newDir.split('\\')[-1]) + (str(num))
                        shutil.copy(newDir, dst)
        else:
            eachTxtFile(newDir)

eachTxtFile(r'F:\Data\Collection')