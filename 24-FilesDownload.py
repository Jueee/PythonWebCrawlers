'''
爬取文件集。
'''
import requests
import re,time,os

USER_NAMBER = 'yunzhan365'      # 子路径
targetDir = 'result\\24-FilesDownload.py\\'+USER_NAMBER    #文件保存路径  

# 获取保存路径
def destFile(path,name=''):
    if not os.path.isdir(targetDir):
        os.makedirs(targetDir)
    pos = path.rindex('/')
    pom = path.rindex('.')
    if name=='':
        t = os.path.join(targetDir, path[pos+1:])
    else:
        t = os.path.join(targetDir, name + '.' + path[pom+1:])
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
    for n in range(1,99):
        album_url = 'https://book.yunzhan365.com/pcqz/stgm/files/mobile/'+str(n)+'.jpg'
        saveImage(album_url, str(n).zfill(4))
            