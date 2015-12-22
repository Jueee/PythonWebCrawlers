'''
http://www.yiibai.com/python/python3-webbug-series4.html
'''

'''
我们用 Python 来登录网站, 用Cookies记录登录信息, 然后就可以抓取登录之后才能看到的信息. 

'''
'''
第一步: 使用 Fiddler 观察浏览器行为


'''
import urllib.request

# 写一个 GET 程序, 把知乎首页 GET 下来
if __name__ != '__main__':
    url = 'https://www.zhihu.com'
    data = urllib.request.urlopen(url).read()
    print(data)

'''
解压缩

知乎网传给我们的是经过 gzip 压缩之后的数据. 这样我们就需要先对数据解压. 

Python 进行 gzip 解压很方便, 因为内置有库可以用. 代码片段如下:
'''
import gzip

def ungzip(data):
    try:        # 尝试解压
        print('正在解压...')
        data = gzip.decompress(data)
        print('解压完毕！')
    except:
        print('无需解压！')
    return data

if __name__ != '__main__':
    url = 'https://www.zhihu.com'
    data = urllib.request.urlopen(url).read()
    print(ungzip(data))


'''
使用正则表达式获取 _xsrf 的值.

我们在第一遍 GET 的时候可以从响应报文中的 HTML 代码里面得到这个 _xsrf 的值. 
如下函数实现了这个功能, 返回的 str 就是 _xsrf 的值.
'''
import re

def getXSRF(data):
    cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]

'''
发射 POST !!

集齐 _xsrf, id, password 三大法宝, 我们可以发射 POST 了. 
这个 POST 一旦发射过去, 我们就登陆上了服务器, 服务器就会发给我们 Cookies. 
本来处理 Cookies 是个麻烦的事情, 不过 Python 的 http.cookiejar 库给了我们很方便的解决方案, 
只要在创建 opener 的时候将一个 HTTPCookieProcessor 放进去, Cookies 的事情就不用我们管了. 
'''
import http.cookiejar
import urllib.request

'''
getOpener 函数接收一个 head 参数, 这个参数是一个字典. 
函数把字典转换成元组集合, 放进 opener. 

这样我们建立的这个 opener 就有两大功能:
1、自动处理使用 opener 过程中遇到的 Cookies
2、自动在发出的 GET 或者 POST 请求中加上自定义的 Header
'''
def getOpener(head):
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


'''
第四部: 正式运行

我们要把要 POST 的数据弄成 opener.open() 支持的格式. 所以还要  urllib.parse 库里的 urlencode() 函数.
这个函数可以把 字典 或者 元组集合 类型的数据转换成 & 连接的 str.
str 还不行, 还要通过 encode() 来编码, 才能当作 opener.open() 或者 urlopen() 的 POST 数据参数来使用.
'''
header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'www.zhihu.com',
    'DNT': '1'
}

url ='http://www.zhihu.com/'
opener = getOpener(header)
op = opener.open(url)
data = op.read()
data = ungzip(data)


_xsrf = getXSRF(data.decode())
print(_xsrf)

url += '/login/email'
id = '921550356@qq.com'
password = 'aa'
postDict = {
    '_xsrf':_xsrf,
    'email':id,
    'password':password,
    'remember_me':True
}

postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url, postData)
data = op.read()
data = ungzip(data)

print(data.decode(()))