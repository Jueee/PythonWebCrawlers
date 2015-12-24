'''
百度搜索框理想词的获取
'''

import urllib.request
import re

def get_baidu_lenovo(codeStr):
    pass
    # urllib的quote()方法控制对特殊字符的URL编码
    # 如将"百度"编码为"%E7%99%BE%E5%BA%A6"
    gjc = urllib.request.quote(codeStr)
    url = 'http://suggestion.baidu.com/su?wd=' + gjc + '&json=1&p=3&sid=&cb=jQuery110205425511478908079_1396251136074&_=1396251136078'  
    headers = {  
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',  
        'Accept' : '*/*',  
        'Connection' : 'Keep-Alive'  
    }
    
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req).read().decode('gbk')
    lenovoStr = re.search(r'"s":\[(.*?)\]', html).group(1)
    print('“%s”的理想词为：%s' % (codeStr, lenovoStr))

codelist = ['百度','谷歌','GitHub','老罗','韩寒','%']
for i in codelist:
    get_baidu_lenovo(i)
'''
运行结果为：

“百度”的理想词为："百度云","百度翻译","百度地图","百度杀毒","百度卫士","百度音乐","百度网盘","百度文库","百度糯米","百度外卖"
“谷歌”的理想词为："谷歌翻译","谷歌地图","谷歌浏览器","谷歌地球","谷歌学术","谷歌僵尸地图","谷歌浏览器官方下载","谷歌地图高清卫星地图","谷歌邮箱","谷歌搜索"
“GitHub”的理想词为："github for windows","github 教程","github desktop","github 下载","github中文网","github使用教程","github for mac","github desktop 教程","github是什么","github删除repository"
“老罗”的理想词为："老罗语录","老罗的android之旅","老罗英语培训","老罗android视频教程","老罗三句名言","老罗斯福","老罗android开发视频教程","老罗英语培训网站","老罗微博","老罗android"
“韩寒”的理想词为："韩寒女儿","韩寒后会无期","韩寒 对话","韩寒吧","韩寒现象","韩寒经典语录","韩寒餐厅被罚","韩寒 白龙马","韩寒电影","韩寒博客"
“%”的理想词为："%s","%d","%2c","%g","%a","%x","%windir%","%f","%20","%u"
'''
