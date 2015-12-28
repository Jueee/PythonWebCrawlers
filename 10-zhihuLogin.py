from urllib import request
import re, time,requests

_Zhihu_URL = 'https://www.zhihu.com'
_Login_URL = _Zhihu_URL + '/#signin'
_Captcha_URL_Prefix = _Zhihu_URL + '/captcha.gif?r=' 
_Cookies_File_Name = 'cookies.json'

_session = None
_header = {'X-Requested-With': 'XMLHttpRequest',
           'Referer': 'http://www.zhihu.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; '
                         'Trident/7.0; Touch; LCJB; rv:11.0)'
                         ' like Gecko',
           'Host': 'www.zhihu.com'}

def getXSRF(data):
    _xsrf = re.search('name=\"_xsrf\" value=\"(.*?)\"', data).group(1)
    return _xsrf

def get_captcha_url():
    return _Captcha_URL_Prefix + str(int(time.time() * 1000))

def save_captcha(url):
    global _session
    r = _session.get(url)
    with open('code.gif', 'wb') as f:
        f.write(r.content)

# 不使用cookies.json，手动登陆知乎
def login(email='',password='',captcha='',savecookies=True):
    global _session
    global _header
    data = {'email':email,'password':password,'remember_me':'true','captcha':captcha}
    r = _session.post(_Login_URL, data=data)
    j = r.json()
    c = int(j['r'])
    m = j['msg']
    if c==0 and savecookies is True:
        with open(_Cookies_File_Name,'w') as f:
            json.dump(_session.cookies.get_dict(),f)
    return c,m

# 创建cookies文件
def create_cookies():
    if os.path.isfile(_Cookies_File_Name) is False:
        email=''
        password=''
        url=get_captcha_url()
        save_captcha(url)
        print('已经生成验证码')
        captcha = input('captcha:')
        code, msg = login(email,password,captcha)
        if code == 0:
            print('cookies 文件创建成功！')
        else:
            print(msg)
        os.remove('code.gif')
    else:
        print('请先删除验证码文件：[%s]' % _Cookies_File_Name)

def init():
    global _session
    if _session is None:
        _session = request.session()
        _session.headers.update(_header)
        if os.path.isfile(_Cookies_File_Name):
            with oppen(_Cookies_File_Name,'r') as f:
                cookie_dict = json.load(f)
                _session.cookies.update(cookie_dict)
        else:
            print('没有cookies文件。')
            print('')
            _session.post(_Login_URL, data={})
    else:
        raise Exception('call init func two times')

init()