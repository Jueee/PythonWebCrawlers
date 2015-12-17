import urllib.request

# 获取页码状态和源码
if __name__ == '__main__':
    url = 'http://baidu.com'
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    
    with urllib.request.urlopen(url) as f:
        print(f.read())
