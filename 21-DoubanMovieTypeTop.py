'''
按类别爬取豆瓣评分最高的电影(使用Beautiful Soup)

'''

import urllib.request
from bs4 import BeautifulSoup
import re,json
import xlwt


DOUBAN_MOVIE = 'http://movie.douban.com'

class Movie(object):
    rank = '0'
    title = ''
    regions = ''
    types = ''
    url = ''
    release_date = ''
    score = ''

class MovieType(object):
    type_name = ''
    type_url = ''
    type_num = ''

def get_movie_type():
    movieTypeList = []
    url = DOUBAN_MOVIE + '/chart'
    html = urllib.request.urlopen(url).read().decode().encode('gbk','ignore').decode('gbk')
    soup = BeautifulSoup(html, "lxml")
    types = soup.find('div', class_='types')
    soup_type = BeautifulSoup(repr(types), "lxml")
    url_types = soup_type.find_all('a')
    for url_type in url_types:
        movieType = MovieType()
        url_soup = BeautifulSoup(repr(url_type), "lxml")
        movieType.type_name = url_soup.find('a').string
        movieType.type_url = DOUBAN_MOVIE + url_soup.a['href']
        movieType.type_num = re.search(r'type=(\d+)&', movieType.type_url).group(1)
        movieTypeList.append(movieType)
    return movieTypeList
# http://movie.douban.com/j/chart/top_list?type=3&interval_id=100%3A90&action=&start=40&limit=20

def get_typeTopMovie(typenum):
    movieList = []
    for i in range(20):
        url = DOUBAN_MOVIE + '/j/chart/top_list?type='+typenum+'&interval_id=100%3A90&action=&start='+str(i*20)+'&limit=20'
        html = urllib.request.urlopen(url).read().decode().encode('gbk','ignore').decode('gbk')
        if html == '[]':
            break
        jsons = json.loads(html)
        for x in range(len(jsons)):
            movie = Movie()
            js = jsons[x]
            movie.rank = js['rank']
            movie.title = js['title']
            movie.regions = js['regions'][0]
            movie.url = js['url']
            movie.release_date = js['release_date']
            movie.score = js['score']
            movie.vote_count = js['vote_count']
            print(movie.rank,movie.score,movie.title)
            movieList.append(movie)
    return movieList


def get_TopMovie_excel():
    wbk = xlwt.Workbook()
    movieTypes = get_movie_type()
    for x in range(len(movieTypes)):
#   for x in range(2):
        movieType = movieTypes[x]
        sheet = wbk.add_sheet(movieType.type_name)
        sheet.write(0,0,'排序')
        sheet.write(0,1,'电影名')
        sheet.write(0,2,'评分')
        sheet.write(0,3,'评分人数')
        sheet.write(0,4,'上映国家')
        sheet.write(0,5,'上映日期')
        sheet.write(0,6,'页面URL')
        movie_lists = get_typeTopMovie(movieType.type_num)
        for x in range(len(movie_lists)):
            movie = movie_lists[x]
            sheet.write(x+1, 0, movie.rank)
            sheet.write(x+1, 1, movie.title)
            sheet.write(x+1, 2, movie.score)
            sheet.write(x+1, 3, movie.vote_count)
            sheet.write(x+1, 4, movie.regions)
            sheet.write(x+1, 5, movie.release_date)
            sheet.write(x+1, 6, movie.url)
        print('生成 %s 类型电影成功！' % movieType.type_name)
    wbk.save('result//21-DoubanMovieTypeTop//DoubanMovieTypeTop.xls')
    print('生成 Excel 成功！')


if __name__ == '__main__':
    #get_movie_type()
    #get_typeTopMovie('3')
    get_TopMovie_excel()