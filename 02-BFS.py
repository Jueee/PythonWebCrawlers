'''
http://www.yiibai.com/python/python3-webbug-series2.html
'''

'''
Python的队列

在爬虫程序中, 用到了广度优先搜索(BFS)算法. 这个算法用到的数据结构就是队列.

Python的List功能已经足够完成队列的功能, 可以用 append() 来向队尾添加元素, 可以用类似数组的方式来获取队首元素, 可以用 pop(0) 来弹出队首元素. 

但是List用来完成队列功能其实是低效率的, 因为List在队首使用 pop(0) 和 insert() 都是效率比较低的.
Python官方建议使用collection.deque来高效的完成队列任务.
'''
from collections import deque

queue = deque(['Eric','John','Michael'])
queue.append('Terry')
queue.append('Graham')
queue.popleft()
print(queue)
queue.popleft()
print(queue)



'''
Python的集合

在爬虫程序中, 为了不重复爬那些已经爬过的网站, 我们需要把爬过的页面的url放进集合中.
在每一次要爬某一个url之前, 先看看集合里面是否已经存在. 
如果已经存在, 我们就跳过这个url; 如果不存在, 我们先把url放入集合中, 然后再去爬这个页面.

Python提供了set这种数据结构. set是一种无序的, 不包含重复元素的结构. 
一般用来测试是否已经包含了某元素, 或者用来对众多元素们去重. 
与数学中的集合论同样, 他支持的运算有交, 并, 差, 对称差.


创建一个set可以用 set() 函数或者花括号 {} . 
但是创建一个空集是不能使用一个花括号的, 只能用 set() 函数. 
因为一个空的花括号创建的是一个字典数据结构. 
'''
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)   # 这里演示的是去重功能
print('orange' in basket)  # 快速判断元素是否在集合内
print('ornage' in basket)  # 快速判断元素是否在集合内

# 下面展示两个集合间的运算.
a = set('abracadabra')
b = set('alacazam')
print(a)        # 集合a中包含元素
print(a - b)
print(a|b)      # 集合a或b中包含的所有元素
print(a & b)    # 集合a和b中都包含了的元素
print(a ^ b)    # 不同时包含于a和b的元素


'''
Python的正则表达式

在爬虫程序中, 爬回来的数据是一个字符串, 字符串的内容是页面的html代码. 
我们要从字符串中, 提取出页面提到过的所有url. 
这就要求爬虫程序要有简单的字符串处理能力, 而正则表达式可以很轻松的完成这一任务.

http://deerchao.net/tutorials/regex/regex.html
http://www.w3cschool.cc/python/python-reg-expressions.htmll
http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html
'''


'''
Python网络爬虫Ver 1.0 alpha
'''
import re
import urllib.request
import urllib
from collections import deque

queue = deque()
visited = set()

url = 'http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html'  # 入口页面, 可以换成别的

queue.append(url)
cnt = 0

while queue:
    url = queue.popleft()   # 队首元素出队
    visited |= {url}        # 标记为已访问

    print('已经抓取：'+str(cnt)+'正在抓取<---'+url)
    cnt += 1
    urlop = urllib.request.urlopen(url)
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


'''
爬虫是可以工作了, 但是在碰到连不上的链接的时候, 它并不会超时跳过. 
而且爬到的内容并没有进行处理, 没有获取对我们有价值的信息, 也没有保存到本地. 
下次我们可以完善这个alpha版本.
'''



