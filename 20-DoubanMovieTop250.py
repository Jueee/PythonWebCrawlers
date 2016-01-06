'''
爬取豆瓣评分最高的250部电影(使用Beautiful Soup)

'''

import urllib.request
from bs4 import BeautifulSoup
import xlwt

MOVIE_TOP250 = 'http://movie.douban.com/top250?start='

class Movie(object):
    id = '0'
    title = ''
    url = ''
    year = ''
    director = ''
    peoples = ''
    rating = ''

        

def get_douban_movie(url,title=''):
    try:
        html = urllib.request.urlopen(url).read().decode().encode('gbk','ignore').decode('gbk')
        soup = BeautifulSoup(html, "lxml")
        title = soup.find('span', property='v:itemreviewed').string
        year = soup.find('span', class_='year').string
        peoples = soup.find('span', property='v:votes').string
        rating = soup.find('strong', class_='ll rating_num').string
        director = soup.find('a', rel='v:directedBy').string
        stars = soup.find_all('span', class_='rating_per')
        return {'title':title,'year':year,'director':director,'peoples':peoples,'rating':rating,'star5':stars[0].string,'star4':stars[1].string,'star3':stars[2].string,'star2':stars[3].string,'star1':stars[4].string}
    except urllib.error.HTTPError as e:
        pass#print('没有该页面：%s' % id)
    except IndexError as e:
        pass#print('字符串超长')
    except UnboundLocalError as e:
        pass
    except Exception as e:
        raise e
    return {'title':title+'[页面失效]','year':'(0000)','director':'','peoples':'0','rating':'0.0','star5':'','star4':'','star3':'','star2':'','star1':''}


def get_movie_list():
    movie_list = []
    for i in range(10):
        top250html = urllib.request.urlopen(MOVIE_TOP250+str(i*25)).read().decode().encode('gbk','ignore').decode('gbk')
        soup = BeautifulSoup(top250html, "lxml")
        itemlist = soup.find_all('div', class_='pic')
        for i in range(len(itemlist)):
            soupitem = BeautifulSoup(repr(itemlist[i]), "lxml")
            num = soupitem.find('em').string
            url = soupitem.a['href']
            title = soupitem.img['alt']
            movie = get_douban_movie(url,title)
            print('%3s，%6s，%6s，%3s，%-50s' % (num,movie.get('year'),movie.get('peoples'),movie.get('rating'),movie.get('title')))
            movie_list.append(movie)
    return movie_list 

def get_movie_top250():
    movie_list = []
    for i in range(10):
        top250html = urllib.request.urlopen(MOVIE_TOP250+str(i*25)).read().decode().encode('gbk','ignore').decode('gbk')
        soup = BeautifulSoup(top250html, "lxml")
        itemlist = soup.find_all('div', class_='pic')
        for i in range(len(itemlist)):
            movie = Movie()
            soupitem = BeautifulSoup(repr(itemlist[i]), "lxml")
            movie.id = soupitem.find('em').string
            movie.url = soupitem.a['href']
            movie.title = soupitem.img['alt']
            movie.rating = soup.find('span', class_='rating_num').string
            movie_list.append(movie)
            print(movie.id,movie.rating,movie.title,movie.url)
    return movie_list

# 生成a,b两个jdid之间的Excel
def get_movie_list_excel():
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet 1')
    sheet.write(0,0,'排序')
    sheet.write(0,1,'电影名')
    sheet.write(0,2,'出品年份')
    sheet.write(0,3,'导演')
    sheet.write(0,4,'评分人数')
    sheet.write(0,5,'总评分')
    sheet.write(0,6,'五星占比')
    sheet.write(0,7,'四星占比')
    sheet.write(0,8,'三星占比')
    sheet.write(0,9,'二星占比')
    sheet.write(0,10,'一星占比')
    movie_lists = get_movie_list()
    for x in range(len(movie_lists)):
        sheet.write(x+1, 0, x+1)
        sheet.write(x+1, 1, movie_lists[x].get('title'))
        sheet.write(x+1, 2, movie_lists[x].get('year'))
        sheet.write(x+1, 3, movie_lists[x].get('director'))
        sheet.write(x+1, 4, movie_lists[x].get('peoples'))
        sheet.write(x+1, 5, movie_lists[x].get('rating'))
        sheet.write(x+1, 6, movie_lists[x].get('star5'))
        sheet.write(x+1, 7, movie_lists[x].get('star4'))
        sheet.write(x+1, 8, movie_lists[x].get('star3'))
        sheet.write(x+1, 9, movie_lists[x].get('star2'))
        sheet.write(x+1, 10, movie_lists[x].get('star1'))
    wbk.save('result//20-DoubanMovieTop250//DoubanMovieTop250.xls')
    print('生成 Excel 成功！')


if __name__ != '__main__':
    get_movie_list_excel()
    
if __name__ == '__main__':
    get_movie_top250()