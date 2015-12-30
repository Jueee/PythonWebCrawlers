'''
在Python中使用Chrome浏览器已有的Cookies发起HTTP请求。
'''
'''
Chrome的Cookies文件保存路径类似于:
'''
#C:\Users\Jueee\AppData\Local\Google\Chrome\User Data\Default\Cookies
#其中C:\Users\Jueee\AppData可通过环境变量os.environ[‘LOCALAPPDATA’]获取。
'''
Cookies是一个Sqlite3数据库文件。
了解完上述事实，问题就非常简单了：
从数据库中查询到所需的Cookies，更新到一个CookieJar对象中。再使用这个CookieJar创建opener即可。
'''

import os
import sqlite3
import http.cookiejar
import http.cookies
import urllib.request
import re
import win32crypt
import requests

def get_chrome_cookies(domain=None):
    cookie_file_path = os.path.join(os.environ['LOCALAPPDATA'],r'Google\Chrome\User Data\Default\Cookies')
    print('Cookies文件的地址为：%s' % cookie_file_path)
    if not os.path.exists(cookie_file_path):
        raise Exception('Cookies 文件不存在...')
    coon = sqlite3.connect(cookie_file_path)
    sql = 'select host_key,name,value,path,encrypted_value from cookies'
    if domain:
        sql += ' where host_key like "%{}%"'.format(domain)
    cookiejar = http.cookiejar.CookieJar()
    for row in coon.execute(sql):
        ret = win32crypt.CryptUnprotectData(row[4], None, None, None, 0)
        cookie_item = http.cookiejar.Cookie(
            version=0,
            name=row[1],
            value=ret[1].decode(),
            port=None,
            port_specified=None,
            domain=row[0],
            domain_specified=None,
            domain_initial_dot=None,
            path=row[3],
            path_specified=None,
            secure=None,
            expires=None,
            discard=None,
            comment=None,
            comment_url=None,
            rest=None,
            rfc2109=False
        )
        cookiejar.set_cookie(cookie_item)
    coon.close()
    return urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookiejar))


get_url='http://www.zhihu.com/people/jueee/answers'
opener = get_chrome_cookies('.zhihu.com')
html_doc = opener.open(get_url).read().decode('utf-8','ignore')

print(html_doc)


for match in re.finditer(r'<a class="question_link".*?href="(.*?)">(.*?)</a>', html_doc):
    link = match.group(1)
    title = match.group(2)
    print(link,title)