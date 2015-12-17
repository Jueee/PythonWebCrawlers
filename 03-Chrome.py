'''
http://www.yiibai.com/python/python3-webbug-series3.html
'''
'''
上一次我自学爬虫的时候, 写了一个简陋的勉强能运行的爬虫alpha. 
alpha版有很多问题：
1、比如一个网站上不了, 爬虫却一直在等待连接返回response, 不知道超时跳过; 
2、或者有的网站专门拦截爬虫程序, 我们的爬虫也不会伪装自己成为浏览器正规部队; 
3、并且抓取的内容没有保存到本地, 没有什么作用
'''

import re
import urllib.request
import http.cookiejar
import urllib
from collections import deque


'''
添加超时跳过功能

首先, 我简单地将
urlop = urllib.request.urlopen(url)
改为
urlop = urllib.request.urlopen(url, timeout = 2)

运行后发现, 当发生超时, 程序因为exception中断

于是我把这一句也放在try .. except 结构里, 问题解决.
'''

'''
支持自动跳转

在爬 http://baidu.com 的时候, 爬回来一个没有什么内容的东西, 这个东西告诉我们应该跳转到 http://www.baidu.com . 
但是我们的爬虫并不支持自动跳转, 现在我们来加上这个功能, 让爬虫在爬 baidu.com 的时候能够抓取 www.baidu.com 的内容.

首先我们要知道爬 http://baidu.com 的时候他返回的页面是怎么样的, 这个我们既可以用 Fiddler 看, 也可以写一个小爬虫来抓取. 
b'<html>\n
    <meta http-equiv="refresh" content="0;url=http://www.baidu.com/">\n
  </html>\n'
利用 html 的 meta 来刷新与重定向的代码, 其中的0是等待0秒后跳转, 也就是立即跳转. 
'''

'''
伪装浏览器正规军

现在详细研究一下如何让网站们把我们的Python爬虫当成正规的浏览器来访. 
因为如果不这么伪装自己, 有的网站就爬不回来了. 
如果看过理论方面的知识, 就知道我们是要在 GET 的时候将 User-Agent 添加到header里.

在 GET 的时候添加 header 有很多方法, 下面介绍两种方法.
'''

'''
第一种方法比较简便直接, 但是不好扩展功能, 代码如下:

'''
if __name__ != '__main__':
    url = 'http://www.baidu.com/'
    req = urllib.request.Request(url, headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    })
    oper = urllib.request.urlopen(req)
    data = oper.read()
    print(data)    

'''
第二种方法使用了 build_opener 这个方法, 用来自定义 opener, 这种方法的好处是可以方便的拓展功能.
例如下面的代码就拓展了自动处理 Cookies 的功能.
'''
if __name__ == '__main__':
    # head: dict of header
    def makeMyOpener(head = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }):
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        header = []
        for key, value in head.items():
            elem = (key, value)
            header.append(elem)
        opener.addheaders = header
        return opener
     
    oper = makeMyOpener()
    uop = oper.open('http://www.baidu.com/', timeout = 1000)
    data = uop.read()
    print(data)


'''

'''
if __name__!='__main__':
    data = urllib.request.urlopen('http://baidu.com').read()
    print(data)
    
    
    queue = deque()
    visited = set()
    
    url = 'http://www.jueee.site/'  # 入口页面, 可以换成别的
    
    queue.append(url)
    cnt = 0
    
    while queue:
        url = queue.popleft()   # 队首元素出队
        visited |= {url}        # 标记为已访问
    
        print('已经抓取：'+str(cnt)+'正在抓取<---'+url)
    
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    
        cnt += 1
        try:
            urlop = urllib.request.urlopen(req, timeout = 2)
        except:
            continue
        
        # 用getheader()函数来获取抓取到的文件类型, 是html再继续分析其中的链接
        if 'html' not in urlop.getheader('Content-Type'):
            continue
        
        # 避免程序异常中止, 用try..catch处理异常
        try:
            data = urlop.read().decode('utf-8')
        except:
            continue
    
        # 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
        linkre = re.compile('href=\"(.+?)\"')
        for x in linkre.findall(data):
            if 'http' in x and x not in visited:
                queue.append(x)
                print('加入队列 --->  ' + x)

