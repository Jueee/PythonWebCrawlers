'''
爬取新浪微博某个用户的头像相册（通过分析API JSON）。
'''
'''

'''
import ChromeCookies
import requests
import re,time,os


USER_NAMBER = '1800591743'      # 微博ID，如“1955032717”

targetDir = 'result\\18-WeiboAnalbum.py\\'+USER_NAMBER    #文件保存路径  

# 获取保存路径
def destFile(path,name=''):
    if not os.path.isdir(targetDir):
        os.mkdir(targetDir)
    pos = path.rindex('/')
    if name=='':
        t = os.path.join(targetDir, path[pos+1:])
    else:
        t = os.path.join(targetDir, name)
    return t

# 保存图片
def saveImage(imgUrl,name=''):
    response = requests.get(imgUrl, stream=True)
    image = response.content
    imgPath = destFile(imgUrl,name)
    try:
        with open(imgPath ,"wb") as jpg:
            jpg.write(image)
            print('保存图片成功！%s' % imgPath)     
            return
    except IOError:
        print('保存图片成功！%s' % imgUrl)   
        return
    finally:
        jpg.close        

if __name__=='__main__':
    DOMAIN_NAME = '.weibo.com'
    cookies = ChromeCookies.get_chrome_cookies(DOMAIN_NAME)
    album_url = 'http://photo.weibo.com/photos/get_latest?uid='+USER_NAMBER
    response = requests.get(album_url, cookies=cookies)
    html_doc = response.text.encode('gbk','ignore').decode('gbk')
    imgnum = re.search(r'"total":(.*?),', html_doc).group(1)
    print(imgnum)
    for n in range(int(imgnum)//20+1):
        page = n+1
        get_url = album_url + '&page='+str(page)
        response = requests.get(get_url, cookies=cookies)

        html_doc = response.text.encode('gbk','ignore').decode('gbk')
        for match in re.finditer(r'"pic_name":"(.*?)"', html_doc,re.S):
            picture = match.group(1)
            pictureurl = 'http://ww3.sinaimg.cn/mw690/'+picture
            saveImage(pictureurl)