#Merge all .xlsx files in the current dir into Merge.csv

import os
import xlrd
import codecs

def list_xlsx_files(rootdir):
    _files = []
    _list = os.listdir(rootdir)
    for i in range(0,len(_list)):
           path = os.path.join(rootdir,_list[i])
           if os.path.isdir(path):
               _files.extend(list_xlsx_files(path))
           if os.path.isfile(path):
               if os.path.splitext(path)[1] == '.xlsx':
                   _files.append(path)
    return _files

def read_xlsx_files(_file):
    workbook = xlrd.open_workbook(_file, 'utf-8')
    booksheet = workbook.sheet_by_index(0)
    row =booksheet.nrows
    xlsx_list = []
    for r in range(row):
        rowdata = booksheet.row_values(r)
        xlsx_list.append(rowdata)
    return(xlsx_list)

def write_csv_files(xlsx_list):
    for i in range(len(xlsx_list)):
        with codecs.open('Merge.csv', 'a', encoding='utf-8') as f:
            for j in range(len(xlsx_list[i])):
                f.write(str(xlsx_list[i][j]))
                f.write(',')
            f.write('\n')
            

if __name__ == "__main__":
    DIR = os.getcwd()
    xlsx_list = []
    for f in list_xlsx_files(DIR):
        print('Reading file(' ,os.path.abspath(f), ')')
        xlsx_list = read_xlsx_files(f)
        write_csv_files(xlsx_list)
