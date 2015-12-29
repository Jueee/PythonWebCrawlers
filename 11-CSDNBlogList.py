'''
根据用户名，获取该用户的CSDN的博客列表
'''

import urllib.request
import re

CSDN_URL = 'http://blog.csdn.net'

# 获取主页网址
def get_blog_url(bloger):
    return 'http://blog.csdn.net/'+bloger+'/article/list'

# 根据网址获取HTML
def get_blog_html(url):
    headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }
    req = urllib.request.Request(url, headers = headers)
    html = urllib.request.urlopen(req).read().decode()
    return html

# 获取页码
def get_page_num(html):
    page = re.search(r'共(\d+)页', html).group(1)
    return page

# 获取博客发表时间
def get_blog_time(html):
    blogtime = re.search(r'<span class="link_postdate">(.*?)</span>', html).group(1)
    return blogtime

# 获取博客阅读次数
def get_blog_reader(html):
    reader = re.search(r'<span class="link_view".*?>(.*?)</span>', html).group(1)
    return reader

# 获取页面列表
def get_blog_list(html):
    content = re.search(r'<span class="link_title"><a href="(.*?)">\s*([^\s]*)\s*</a></span>', html)
    for match in re.finditer(r'<span class="link_title"><a href="(.*?)">\s*([^\s]*)\s*</a></span>', html):
        link = match.group(1)
        title = match.group(2)
        blogurl = CSDN_URL + link
        bloghtml = get_blog_html(blogurl)
        blogtime = get_blog_time(bloghtml)
        blogreader = get_blog_reader(bloghtml)
        print('%s %s %+10s %-50s' % (link,blogtime,blogreader,title))

if __name__ == '__main__':
    bloger = 'oYunTaoLianWu'
    blogurl = get_blog_url(bloger)
    html = get_blog_html(blogurl)
    page = get_page_num(html)
    for x in range(int(page)):
        pageurl = blogurl + '/' + str(x+1)
        print('第%s页的博客目录如下(%s)：' % (x+1,pageurl))
        html = get_blog_html(pageurl)
        get_blog_list(html)


'''
运行结果：

第1页的博客目录如下(http://blog.csdn.net/oYunTaoLianWu/article/list/1)：
/jueblog/article/details/33700479 2014-06-23 09:07     916人阅读 notepad++列块编辑操作                                   
/jueblog/article/details/26486821 2014-05-21 17:17     891人阅读 【Chrome】Chrome插件开发（一）插件的简单实现                      
/jueblog/article/details/17465225 2013-12-21 13:40    3137人阅读 【Java】实现按中文首字母排序                                  
/jueblog/article/details/16972635 2013-11-26 22:04    7031人阅读 【实用技术】WIN7系统下U盘安装了ubuntu13.04双系统                  
/jueblog/article/details/16103925 2013-11-13 22:04    1171人阅读 【Android】Android蓝牙开发深入解析                          
/jueblog/article/details/15013635 2013-11-09 23:27    2038人阅读 【Android】App自动更新之通知栏下载                            
/jueblog/article/details/14600521 2013-11-08 23:27    2491人阅读 【Android】网络图片加载优化（一）利用弱引用缓存异步加载                   
/jueblog/article/details/14497181 2013-11-07 22:43    8588人阅读 【Android】第三方QQ账号登录的实现                             
/jueblog/article/details/13434551 2013-10-29 00:26    6374人阅读 【Java】内部类与外部类的互访使用小结                              
/jueblog/article/details/13164349 2013-10-27 02:08    8249人阅读 【Android】PULL解析XML文件                              
/jueblog/article/details/12985045 2013-10-24 01:06   16847人阅读 【Android】Web开发之使用WebView控件展示Web页面                 
第2页的博客目录如下(http://blog.csdn.net/oYunTaoLianWu/article/list/2)：
/jueblog/article/details/12984417 2013-10-24 00:50    1396人阅读 【Android】Wifi管理与应用                                
/jueblog/article/details/12983821 2013-10-24 00:38    1670人阅读 【Android】Web开发之通知栏下载更新APP                         
/jueblog/article/details/12958737 2013-10-23 00:54    2754人阅读 【Android】Web开发之显示网络图片的两种方法                        
/jueblog/article/details/12958159 2013-10-23 00:40    2658人阅读 【Android】Web开发之通过Apache接口处理Http请求                 
/jueblog/article/details/12847239 2013-10-18 01:09    3142人阅读 【Android】MediaPlayer使用方法简单介绍                      
/jueblog/article/details/12806909 2013-10-17 00:29    2334人阅读 【Android】Web开发之通过标准Java接口处理Http请求                 
/jueblog/article/details/12764325 2013-10-16 01:23    3012人阅读 【Android】Activity与服务Service绑定                     
/jueblog/article/details/12721651 2013-10-15 00:43    1681人阅读 【Android】利用服务Service创建标题栏通知                       
/jueblog/article/details/12721555 2013-10-15 00:36    2253人阅读 【Android】利用广播Broadcast接收SMS短信                     
/jueblog/article/details/12691855 2013-10-14 01:07    6796人阅读 【Android】利用广播BroadCast监听网络的变化                     
/jueblog/article/details/12668215 2013-10-13 02:34    2909人阅读 【Android】Activity遮罩效果的实现                          
/jueblog/article/details/12667463 2013-10-13 02:28   12967人阅读 【Android】BroadCast广播机制应用与实例                       
/jueblog/article/details/12655269 2013-10-12 17:41    1182人阅读 【Android】Handler应用（四）：AsyncTask的用法与实例             
/jueblog/article/details/12627403 2013-10-12 00:57    3269人阅读 【Android】Handler应用（三）：从服务器端分页加载更新ListView     
'''