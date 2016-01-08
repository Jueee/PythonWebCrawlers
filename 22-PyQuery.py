'''
Python中PyQuery库的使用总结


pyquery库是jQuery的Python实现，可以用于解析HTML网页内容
'''

from pyquery import PyQuery as pq


print('----1.可加载一段HTML字符串，或一个HTML文件，或是一个url地址----')
d1 = pq('<html><title>hello</title></html>')
d2 = pq(url='http://movie.douban.com/subject/1309069/')
#d3 = pq(filename='result\\02-tieba\\16pn=1.html')


print('----2.html()和text() ——获取相应的HTML块或文本块----')
d1 = pq('<html><title>hello</title></html>')
print(d1('html'))           # <html><title>hello</title></html>
print(d1('html').html())    # <title>hello</title>
print(d1('html').text())    # hello


print('----3.根据HTML标签来获取元素----')
d=pq('<div><p>test 1</p><p>test 2</p></div>')
print(d('p'))               # <p>test 1</p><p>test 2</p>
print(d('p').html())        # test 1


print('----4.eq(index) ——根据给定的索引号得到指定元素----')
d=pq('<div><p>test 1</p><p>test 2</p></div>')
print(d('p').html())
print(d('p').eq(0).html())  # test 1
print(d('p').eq(1).html())  # test 2
print(d('p').eq(2).html())  # None


print('----5.filter() ——根据类名、id名得到指定元素----')
d=pq("<div><p id='one'>test 1</p><p class='two'>test 2</p></div>")
print(d('p').filter('#one'))  # <p id="one">test 1</p>
print(d('p').filter('.two'))  # <p class="two">test 2</p>


print('----6.find() ——查找嵌套元素----')
d=pq("<div><p id='one'>test 1</p><p class='two'>test 2</p></div>")
print(d('div').find('p'))       # <p id="one">test 1</p><p class="two">test 2</p>
print(d('div').find('p').eq(0)) # <p id="one">test 1</p>


print('----7.直接根据类名、id名获取元素----')
d=pq("<div><p id='one'>test 1</p><p class='two'>test 2</p></div>")
print(d('#one').html())     # test 1
print(d('.two').html())     # test 2


print('----8.获取属性值----')
d=pq("<p id='my_id'><a href='http://hello.com'>hello</a></p>")
print(d('a').attr('href'))  # http://hello.com
print(d('p').attr('id'))    # my_id

print('----9.修改属性值----')
d=pq("<p id='my_id'><a href='http://hello.com'>hello</a></p>")
print(d)        # <p id="my_id"><a href="http://hello.com">hello</a></p>
d('a').attr('href','http://baidu.com')
print(d)        # <p id="my_id"><a href="http://baidu.com">hello</a></p>


print('----10.addClass(value) ——为元素添加类----')
d=pq('<div></div>')
print(d)                # <div/>
d.addClass('my_class')
print(d)                # <div class="my_class"/>


print('----11.hasClass(name) #返回判断元素是否包含给定的类----')
d=pq("<div class='my_class'></div>")
print(d.hasClass('my_class'))   # True
print(d.hasClass('my_c'))       # False


print('----12.children(selector=None) ——获取子元素----')
d=pq("<span><p id='one'>hello</p><p id='two'>world</p></span>")
print(d.children())             # <p id="one">hello</p><p id="two">world</p>
print(d.children('#two'))       # <p id="two">world</p>


print('----13.parents(selector=None)——获取父元素----')
d=pq("<span><p id='one'>hello</p><p id='two'>world</p></span>")
print(d('p').parents())         # <span><p id="one">hello</p><p id="two">world</p></span>
print(d('#one').parents('span'))# <span><p id="one">hello</p><p id="two">world</p></span>
print(d('#one').parents('p'))   # []


print('----14.clone() ——返回一个节点的拷贝----')
d=pq("<span><p id='one'>hello</p><p id='two'>world</p></span>")
print(d('#one'))                # <p id="one">hello</p>
print(d('#one').clone())        # <p id="one">hello</p>


print('----15.empty() ——移除节点内容----')
d=pq("<span><p id='one'>hello</p><p id='two'>world</p></span>")
print(d)            # <span><p id="one">hello</p><p id="two">world</p></span>
d('#one').empty()
print(d)            # <span><p id="one"/><p id="two">world</p></span>


print('----16.nextAll(selector=None) ——返回后面全部的元素块----')
d=pq("<p id='one'>hello</p><p id='two'>world</p><img scr='' />")
print(d('p:first').nextAll())   # <p id="two">world</p><img scr=""/>
print(d('p:last').nextAll())    # <img scr=""/>

print('----17.not_(selector) ——返回不匹配选择器的元素----')
d=pq("<span><p id='one'>hello</p><p id='two'>world</p></span>")
print(d('p').not_('#two'))      # <p id="one">hello</p>



'''
爬取豆瓣电影页面中主演
'''
if __name__ == '__main__':
    print('----爬取豆瓣电影页面中主演----')
    # 读取Batman Begins页面  
    doc = pq(url='http://movie.douban.com/subject/3077412/')
    # 遍历starring节点  
    starring = doc("a[rel='v:starring']")
    # 转化为Map
    stars = starring.map(lambda i,e:pq(e).text())
    print('<<%s>>的主演：' % (doc("span[property='v:itemreviewed']").text()))
    for i in stars:
        print(i)
'''
执行结果：

----爬取豆瓣电影页面中主演----
<<寻龙诀>>的主演：
陈坤
黄渤
舒淇
杨颖
夏雨
刘晓庆
颜卓灵
曹操
张东
黄西
僧格仁钦
'''