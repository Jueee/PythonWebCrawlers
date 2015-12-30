'''
获取Chrome浏览器已保存的账号和密码。
'''
# Chrome浏览器已保存的密码都保存在一个sqlite3数据库文件中，和Cookies数据库在同一个文件夹.
# C:\Users\Jueee\AppData\Local\Google\Chrome\User Data\Default\Login Data
'''
使用CryptUnprotectData函数解密数据库中的密码字段，即可还原密码，只需要User权限，并且只能是User权限。
'''
'''
为了防止出现读写出错，建议先把数据库临时拷贝到当前目录。
'''
import os,sys
import shutil
import sqlite3
import win32crypt

db_file_path = os.path.join(os.environ['LOCALAPPDATA'],r'Google\Chrome\User Data\Default\Login Data')
print(db_file_path)

tmp_file = os.path.join(os.path.dirname(sys.executable),'tmp_tmp_tmp')
print(tmp_file)
if os.path.exists(tmp_file):
    os.remove(tmp_file)
shutil.copyfile(db_file_path,tmp_file)

conn = sqlite3.connect(tmp_file)
for row in conn.execute('select signon_realm,username_value,password_value from logins'):
    try:
        ret = win32crypt.CryptUnprotectData(row[2],None,None,None,0)
        print('网站：%-50s，用户名：%-20s，密码：%s' % (row[0][:50],row[1],ret[1].decode('gbk')))
    except Exception as e:
        print('获取Chrome密码失败...')
        raise e
conn.close()
os.remove(tmp_file)
