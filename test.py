__author__ = 'ftium4.com'
import sqlite3
import win32crypt
outFile_path=r'D:\chrome_cookies.txt';
sql_file= r'C:\Users\jiangling\AppData\Local\Google\Chrome\User Data\Default\Cookies';
sql_exe="select host_key,name,value,encrypted_value from cookies";
conn = sqlite3.connect(sql_file)
for row in conn.execute(sql_exe):
    pwdHash = str(row[3])
    try:
        ret = win32crypt.CryptUnprotectData(pwdHash, None, None, None, 0)
    except:
        print 'Fail to decrypt chrome cookies'
        sys.exit(-1)
    with open(outFile_path, 'a+') as outFile:
        outFile.write('host_key: {0:<20} name: {1:<20} value: {2} \n\n'.format(
            row[0].encode('gbk'), row[1].encode('gbk'),ret[1].encode('gbk')) )
conn.close()
print 'All Chrome cookies saved to:\n' + outFile_path