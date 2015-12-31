'''
动态爬虫工具 selenium 的安装与使用（通过控制浏览器实现）。
'''
'''
selenium 安装：pip install selenium
'''
'''
selenium 调用浏览器：
调用 Firefox：直接调用 webdriver.Firefox()
调用 Chrome：安装chromedriver.exe后调用 webdriver.Firefox()
             chromedriver.exe下载路径："https://sites.google.com/a/chromium.org/chromedriver/downloads"
             需要将chromedriver.exe 放在chrome浏览器安装目录下，或放到python的安装目录。
            （同时设置用户环境变量path:"C:\\Users\\xxxxxx\\AppData\\Local\\Google\\Chrome\\Application";）
调用 IE：安装IEDriverServer.exe后webdriver.Ie()
         需要将IEDriverServer.exe 放在ie浏览器安装目录下
        （同时设置用户环境变量path："C:\\Program Files\\Internet Explorer" ）
'''
'''
通过id定位元素：find_element_by_id("id_vaule")
通过name定位元素：find_element_by_name("name_vaule")
通过tag_name定位元素：find_element_by_tag_name("tag_name_vaule")
通过class_name定位元素：find_element_by_class_name("class_name")
通过css定位元素：find_element_by_css_selector();用css定位是比较灵活的
通过xpath定位元素：find_element_by_xpath("xpath")
通过link定位：find_element_by_link_text("text_vaule")或者find_element_by_partial_link_text()
'''
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

# selenium 调用浏览器并模拟百度的操作
if __name__ != '__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.find_element_by_id('kw').send_keys('Python开发')
    driver.find_element_by_id('su').click()
    time.sleep(5)
    driver.close()

# 打印cookie信息
if __name__ != '__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    cookie= driver.get_cookies()
    print(cookie)
    driver.close()

# Selenium+PhantomJS使用：
if __name__ == '__main__':
    driver = webdriver.PhantomJS()
    driver.get("http://www.baidu.com")
    print(driver.title)
    driver.quit()