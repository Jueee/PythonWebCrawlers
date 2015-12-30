'''
在Python中使用Chrome浏览器已有的Cookies发起HTTP请求。

参考博客：http://blog.csdn.net/pipisorry/article/details/47980653
'''
import subprocess
import sqlite3
import win32crypt
import re,os
import requests

def get_chrome_cookies(url):
    DIST_COOKIE_FILENAME = '.\python-chrome-cookies'
    SOUR_COOKIE_FILENAME = os.path.join(os.environ['LOCALAPPDATA'],r'Google\Chrome\User Data\Default\Cookies')
    print('Cookies文件的地址为：%s' % SOUR_COOKIE_FILENAME)
    if not os.path.exists(SOUR_COOKIE_FILENAME):
        raise Exception('Cookies 文件不存在...')
    subprocess.call(['copy', SOUR_COOKIE_FILENAME, DIST_COOKIE_FILENAME], shell=True)
    conn = sqlite3.connect(".\python-chrome-cookies")
    ret_dict = {}
    for row in conn.execute("SELECT host_key, name, path, value, encrypted_value FROM cookies"):
        if row[0] != url:
            continue
        ret = win32crypt.CryptUnprotectData(row[4], None, None, None, 0)
        ret_dict[row[1]] = ret[1].decode()
    conn.close()
    subprocess.call(['del', '.\python-chrome-cookies'], shell=True)
    return ret_dict

# 可以无障碍使用
if __name__=='__main__':
    print('------使用requests进行解析访问------')
    DOMAIN_NAME = '.zhihu.com'
    get_url = r'https://www.zhihu.com/people/jueee/answers'
    response = requests.get(get_url, cookies=get_chrome_cookies(DOMAIN_NAME))
    
    html_doc = response.text.encode('gbk','ignore').decode('gbk')
    # print(html_doc)
    
    for match in re.finditer(r'<a class="question_link".*?href="(.*?)">(.*?)</a>', html_doc):
        link = match.group(1)
        title = match.group(2)
        print(link,title)


# 有点小问题，无法登陆
if __name__=='__main__':
    print('------使用 urllib.request 进行解析访问------')
    import urllib.request
    
    DOMAIN_NAME = '.zhihu.com'
    get_url = r'https://www.zhihu.com/people/jueee/answers'
    headers = {'Cookie': ['='.join((i, j)) for i, j in get_chrome_cookies(DOMAIN_NAME).items()][0]}
    request = urllib.request.Request(get_url, headers=headers)
    response = urllib.request.urlopen(request)
    html_doc = response.read().decode().encode('gbk','ignore').decode('gbk')
    print(html_doc)
    
    for match in re.finditer(r'<a class="question_link".*?href="(.*?)">(.*?)</a>', html_doc):
        link = match.group(1)
        title = match.group(2)
        print(link,title)
