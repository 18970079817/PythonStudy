import os
import os.path

start_path = raw_input('Input the start path:')
os.chdir(start_path)
mp3, txt, rar, sql, csv, html, exe, doc, z7, zip, sap, xls, xlsx, db, dat, doc, docx = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
for parentdir,dirname,filenames in os.walk(start_path):
       for filename in filenames:
            if os.path.splitext(filename)[1] == '.mp3':
                mp3 += 1
            elif os.path.splitext(filename)[1] == '.txt':
                txt += 1
            elif os.path.splitext(filename)[1] == '.rar':
                rar += 1
            elif os.path.splitext(filename)[1] == '.sql':
                sql += 1
            elif os.path.splitext(filename)[1] == '.csv':
                csv += 1
            elif os.path.splitext(filename)[1] == '.html':
                html += 1
            elif os.path.splitext(filename)[1] == '.exe':
                exe += 1
            elif os.path.splitext(filename)[1] == '.doc':
                doc += 1
            elif os.path.splitext(filename)[1] == '.7z':
                z7 += 1
            elif os.path.splitext(filename)[1] == '.zip':
                zip += 1
            elif os.path.splitext(filename)[1] == '.sap':
                sap += 1
            elif os.path.splitext(filename)[1] == '.xls':
                xls += 1
            elif os.path.splitext(filename)[1] == '.xlsx':
                xlsx += 1
            elif os.path.splitext(filename)[1] == '.db':
                db += 1
            elif os.path.splitext(filename)[1] == '.dat':
                dat += 1
            elif os.path.splitext(filename)[1] == '.doc':
                doc += 1
            elif os.path.splitext(filename)[1] == '.docx':
                docx += 1
print 'mp3:', mp3
print 'txt:', txt
print 'rar:', rar
print 'sql:', sql
print 'csv:', csv
print 'html:', html
print 'exe:', exe
print 'doc:', doc
print '7z:', z7
print 'zip:', zip
print 'sap:', sap
print 'xls:', xls
print 'xlsx:', xlsx
print 'db:', db
print 'dat:', dat
print 'doc:', doc
print 'docx:', docx