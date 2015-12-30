'''
获取某个用户的知乎回答列表及赞同数
'''

import ChromeCookies
import requests
import re

ZHIHU_URL = 'https://www.zhihu.com'
USER_NAME = 'wangnuonuo'

if __name__=='__main__':
    DOMAIN_NAME = '.zhihu.com'
    cookies = ChromeCookies.get_chrome_cookies(DOMAIN_NAME)
    get_url = ZHIHU_URL + r'/people/'+USER_NAME+'/answers'
    response = requests.get(get_url, cookies=cookies)
    html_doc = response.text.encode('gbk','ignore').decode('gbk')
    answersNum = re.search(r'回答\s<span class="num">(.*?)</span>', html_doc).group(1)
    for num in range(int(answersNum)//20+1):
        answers_url = get_url + '?page='+str(num+1)
        print(answers_url)
        response_answer = requests.get(answers_url, cookies=cookies)
        html_answer = response_answer.text.encode('gbk','ignore').decode('gbk')
        for answermatch in re.finditer(r'<div class="zm-item"([\s\S]*?)<i class="z-icon-fold">', html_answer,re.S):
            answer = answermatch.group(1)
            match1 = re.search(r'<a class="question_link" href="(.*?)">(.*?)</a>', answer)
            link = match1.group(1)
            title = match1.group(2)
            match2 = re.search(r'<a class="zm-item-vote-count js-expand js-vote-count".*?>(.*?)</a>', answer)
            vote = match2.group(1)
            match3 = re.search(r'<a class="answer-date-link[\s\S]*?>(.*?)</a>', answer)
            date = match3.group(1)
            print('问题链接：%s，%s，赞同数：%6s，标题：%-80s' % (link,date,vote,title))

'''
运行结果：


https://www.zhihu.com/people/wangnuonuo/answers?page=1
问题链接：/question/38821362/answer/79145656，发布于 昨天 21:20，赞同数：   215，标题：有哪些尚未普及却非常好用的东西？                                                                
问题链接：/question/30566381/answer/77633766，编辑于 2015-12-20，赞同数：  2624，标题：中国女权发展面临的最大挑战是什么？                                                               
问题链接：/question/35969990/answer/76977890，编辑于 2015-12-16，赞同数：    55，标题：如何评价《万万没想到西游篇》大电影？                                                              
问题链接：/question/19914257/answer/76360974，编辑于 2015-12-11，赞同数：   313，标题：三文鱼怎么做比较好吃？                                                                     
问题链接：/question/20842860/answer/75644153，发布于 2015-12-07，赞同数：   356，标题：猫屎咖啡的确是来源于猫的粪便，为什么人类偏偏独爱猫屎，而不是其他动物屎？猪屎怎么样？                                      
问题链接：/question/38195617/answer/75625923，编辑于 2015-12-07，赞同数：   622，标题：你有过「我要死了吗」的体验吗？                                                                 
问题链接：/question/37201429/answer/73641915，编辑于 2015-12-07，赞同数：  1019，标题：「少数服从多数」这种思维的适用性有多强？                                                            
问题链接：/question/37065743/answer/72566118，编辑于 2015-11-17，赞同数：  3692，标题：怎么样做可以当网红？                                                                      
问题链接：/question/36601352/answer/71744930，编辑于 2015-11-11，赞同数：   665，标题：如何评价王诺诺（朱妍桥）在中华小姐比赛上的表现？

'''