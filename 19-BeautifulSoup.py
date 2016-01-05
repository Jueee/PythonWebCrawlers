'''
Beautiful Soup(python3中的爬虫匹配神器)

参考阅读：Beautiful Soup 中文文档
http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
'''
'''
Beautiful Soup 是用Python写的一个HTML/XML的解析器，它可以很好的处理不规范标记并生成剖析树(parse tree)。 
它提供简单又常用的导航（navigating），搜索以及修改剖析树的操作。它可以大大节省你的编程时间。 
'''
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# 得到一个 BeautifulSoup 的对象
soup = BeautifulSoup(html)
# 按照标准的缩进格式的结构输出
print(soup.prettify())

'''
# 简单的浏览结构化数据的方法:
'''
print(soup.title)
# <title>The Dormouse's story</title>
print(soup.title.name)
# title
print(soup.title.string)
# The Dormouse's story
print(soup.title.parent.name)
# head
print(soup.p)
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
print(soup.p['class'])
# ['title']
print(soup.a)
# <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
print(soup.find_all('a'))
# [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
print(soup.find(id='link3'))
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

# 从文档中找到所有<a>标签的链接:
for link in soup.find_all('a'):
    print(link.get('href'))
'''
http://example.com/elsie
http://example.com/lacie
http://example.com/tillie
'''

# 从文档中获取所有文字内容:
print(soup.get_text())


'''
对象的种类

Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象.
所有对象可以归纳为4种: Tag , NavigableString , BeautifulSoup , Comment .
'''
'''
Tag
Tag 对象与XML或HTML原生文档中的tag相同:
'''
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b
print(type(tag))
# <class 'bs4.element.Tag'>
'''
Name
每个tag都有自己的名字,通过 .name 来获取:
'''
print(tag.name)
# b
# 如果改变了tag的name,那将影响所有通过当前Beautiful Soup对象生成的HTML文档:
tag.name = 'blockquote'
print(tag)
# <blockquote class="boldest">Extremely bold</blockquote>
'''
Attributes
一个tag可能有很多个属性. tag <b class="boldest"> 有一个 “class” 的属性,值为 “boldest” .
tag的属性的操作方法与字典相同:
'''
print(tag['class'])
# ['boldest']
# 也可以直接”点”取属性, 比如: .attrs :
print(tag.attrs)
# {'class': ['boldest']}

tag['class'] = 'verybold'
tag['id'] = 1
print(tag)
# <blockquote class="verybold" id="1">Extremely bold</blockquote>
del tag['id']
print(tag)
# <blockquote class="verybold">Extremely bold</blockquote>
'''
多值属性
'''
css_soup = BeautifulSoup('<p class="body strikeout"></p>')
print(css_soup.p['class'])
# ['body', 'strikeout']
# 如果某个属性看起来好像有多个值,但在任何版本的HTML定义中都没有被定义为多值属性,那么Beautiful Soup会将这个属性作为字符串返回
id_soup = BeautifulSoup('<p id="my id"></p>')
print(id_soup.p['id'])
# my id
# 将tag转换成字符串时,多值属性会合并为一个值
rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>')
print(rel_soup.a['rel'])
# ['index']
rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)
# <p>Back to the <a rel="index contents">homepage</a></p>

'''
可以遍历的字符串
字符串常被包含在tag内.Beautiful Soup用 NavigableString 类来包装tag中的字符串:
'''
print(tag.string)
# Extremely bold
type(tag.string)
# <class 'bs4.element.NavigableString'>
'''
# 通过 unicode() 方法可以直接将 NavigableString 对象转换成Unicode字符串:
unicode_string = unicode(tag.string)
unicode_string
# u'Extremely bold'
type(unicode_string)
# <type 'unicode'>
'''
# tag中包含的字符串不能编辑,但是可以被替换成其它的字符串,用 replace_with() 方法:
tag.string.replace_with("No longer bold")
tag
# <blockquote>No longer bold</blockquote>


print('---------遍历文档树---------')

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html)
'''
遍历文档树
'''
print(soup.head)
print(soup.title)
# 通过点取属性的方式只能获得当前名字的第一个tag:
print(soup.body.b)
# 如果想要得到所有的<a>标签
print(soup.find_all('a'))



# tag的 .contents 属性可以将tag的子节点以列表的方式输出:
head_tag = soup.head
print(head_tag.contents)
print(head_tag.contents[0])
print(head_tag.contents[0].contents)
print(head_tag.contents[0].contents[0])
# 通过tag的 .children 生成器,可以对tag的子节点进行循环:
for child in head_tag.contents[0]:
    print(child)


# .descendants
print('--------.descendants--------')
# .contents 和 .children 属性仅包含tag的直接子节点.
# .descendants 属性可以对所有tag的子孙节点进行递归循环
for child in head_tag.descendants:
    print(child)

# .string
# 如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 .string 得到子节点:
print(head_tag.string)
# 如果tag包含了多个子节点,tag就无法确定 .string 方法应该调用哪个子节点的内容, .string 的输出结果是 None :
print(soup.html.string)




# .strings 和 stripped_strings
# 如果tag中包含多个字符串 [2] ,可以使用 .strings 来循环获取:
for string in soup.strings:
    print(repr(string))

# 输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容:
# [注]全部是空格的行会被忽略掉,段首和段末的空白会被删除
for string in soup.stripped_strings:
    print(repr(string))

# 通过 .parent 属性来获取某个元素的父节点.

