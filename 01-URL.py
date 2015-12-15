'''
用Python抓取指定页面
'''
#encoding:UTF-8
import urllib.request

'''
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False)

urlopen()函数返回一个 http.client.HTTPResponse 对象
'''
# 用Python抓取指定页面的源码
if __name__ != '__main__':
    url = 'http://www.baidu.com'
    data = urllib.request.urlopen(url)
    print(data)
    print(data.info())
    print(type(data))
    print(data.geturl())
    print(data.getcode())
    print(data.read())

# 获取页码状态和源码
if __name__ != '__main__':
    url = 'http://www.douban.com/'
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    
    with urllib.request.urlopen(req) as f:
        print('status:',f.status,f.reason)
        for k,v in f.getheaders():
            print('%s:%s' % (k,v))
        print(f.read().decode('utf-8'))

# 用Python简单处理URL
if __name__=='__main__':
    data = {}
    data['word'] = 'Jecyay Notes'
    url_values = urllib.parse.urlencode(data)
    url = 'http://www.baidu.com'