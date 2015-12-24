from urllib import request, error, parse
import re, hashlib, os

# 百度贴吧爬虫
class Baidu_tieba(object):
    contentType = ''    # 资源类型
    charset = ''        # 资源编码
    filepath = 'result\\02-tieba\\'       # 文件路径
    
    def get_content_header(self, url):
        headers = {  
            'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',  
            'Accept' : '*/*',  
            'Connection' : 'Keep-Alive'  
        }
        req = request.Request(url, headers = headers)
        try:
            resp = request.urlopen(req)
        except error.URLError as e:
            print(e.reason + ':' + e.code)
        else:
            m = re.search('\w+/(\w+).*=(.*)', resp.headers['Content-Type'])
            if m:
                self.contentType = m.group(1)
                self.charset =  m.group(2)
            else:
                print('没有获取文件类型和编码')
            urlstream = resp.read()
        finally:
            resp.close()
        return urlstream

    # 抓取资源
    def fetchtieba(self, url):
        flag = False    # 是否活得页数
        i = 1
        temp = url
        while True:
            params = parse.urlencode({'pn':i})
            url = temp + '?' + str(params)
            res = self.get_content_header(url)
            print('正在抓取：%s' % url)
            if flag == False:
                pages, flag = self.getpages(res)
                self.storeResourse(i, res, url)
            else:
                self.storeResourse(i, res, url)
            if i < pages:
                i += 1
                url = ''
            else:
                print('已经抓取完毕！')
                break

    # 正则获取该贴吧某话题的页面数
    def getpages(self, stream):
        # 将获取的字符串strTxt做decode时，指明ignore，会忽略非法字符
        s = stream.decode(self.charset,'ignore')
        pattern = re.compile('<span class="red">(\d+)</span>')   #正则表达式
        match = pattern.search(s)   # 注意search与match的区别  
        res = [0, False]
        if match:
            pages = int(match.group(1))
            res = [pages, True]
        else:
            print('没有获取页面数！')
        return res

    # 存储资源
    def storeResourse(self, i, stream, url = ''):
        md5 = hashlib.md5()     # 生成md5文件名
        md5.update(str(i).encode(encoding='utf-8', errors='strict'))
        if (os.path.exists(self.filepath) == False):
            os.mkdir(self.filepath)
        pattern = re.compile('(\d+\?pn=\d+)')   #正则表达式
        match = pattern.search(url)   # 注意search与match的区别  
        res = [0, False]
        if match:
            name = match.group(1).replace('?', '')
        else:
            name = md5.hexdigest()
        filename = self.filepath + name + '.' + self.contentType
        f = open(filename, mode='wb+')
        f.write(stream)
        f.close()


baidu = Baidu_tieba()   #实例化对象  
# 输入参数
#input('请输入百度贴吧的地址(http://tieba.baidu.com/p/2782298181):\n')  
bdurl = 'http://tieba.baidu.com/p/1667806599'  
# 调用
baidu.fetchtieba(bdurl)
