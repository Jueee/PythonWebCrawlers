'''
Chrome 33+浏览器 Cookies encrypted_value解密脚本
'''
'''
Chrome浏览器版本33以上对Cookies进行了加密.

用SQLite Developer打开Chrome的Cookies文件就会发现，原来的value字段已经为空，取而代之的是加密的encrypted_value。
'''
import sqlite3
import win32crypt
import os

cookie_file_path = os.path.join(os.environ['LOCALAPPDATA'],r'Google\Chrome\User Data\Default\Cookies')
print('Cookies文件的地址为：%s' % cookie_file_path)
if not os.path.exists(cookie_file_path):
    raise Exception('Cookies 文件不存在...')
sql_exe="select host_key,name,value,path,encrypted_value from cookies";
conn = sqlite3.connect(cookie_file_path)
for row in conn.execute(sql_exe):
    ret = win32crypt.CryptUnprotectData(row[4], None, None, None, 0)
    print('Cookie的Key：%-40s,Cookie名：%-50s，Cookie值：%s' % (row[0],row[1],ret[1].decode()))
conn.close()
