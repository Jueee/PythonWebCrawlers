'''
简单爬虫获取京东的商品价格
'''

'''
方法：通过京东移动商城（因为它没有把价格藏在js中）
'''
import urllib.request
import re

# 通过京东移动接口  
# 参数url：京东原本的商品网址  
def get_jd_price(id):
    url = 'http://item.jd.com/'+str(id)+'.html'        #原本的网址 
    jdid = re.search(r'/(\d+)\.html', url).group(1)      #原本的网址提取出商品ID
    
    url = 'http://m.jd.com/product/'+jdid+'.html'   #转换成为移动商城的url  
    #通过对源代码进行utf-8解码  
    html = urllib.request.urlopen(url).read().decode('utf-8')
    
    # 获取重定向后的地址
    try:
        url = re.search(r'returnUrl=(.*)\"', html).group(1)
        html = urllib.request.urlopen(url).read().decode('utf-8')
    except:
        pass
    
    # 提取商品名称
    m = re.search(r'<span class="title-text">(.*?)<i.*?/i></span>',html,re.S)
    if m:
        jdname = m.group(1)
    
    # 提取出商品价格
    # 匹配时指定re.S可以让点匹配所有字符，包括换行符
    m = re.search(r'<div class="prod-price">.*?<span>(.*?)</span>(.*?)</div>',html,re.S)
    if m:
        jdprice = m.group(2)
    
    print('商品ID：%s' % jdid)
    print('商品名称：%s' % jdname)
    print('商品价格：%s' % jdprice)

id = 1119429
get_jd_price(id)

for x in range(1,10):
    id = 1119452 + x
    get_jd_price(id)


'''
运行效果：

商品ID：1119429
商品名称：丹姿水密码冰川矿泉洁肤晶露100g（洗面奶 深层清洁 温和保湿）  
商品价格：9.90                              
                                            
商品ID：1119453
商品名称：惠普（HP） CN053AA 932XL 超大号黑彩墨盒套装墨盒 （含1支黑，3支彩，购买时彩色显示为附件）  
商品价格：577.00                              
                                            
商品ID：1119454
商品名称：嘉速（Jiasu） 尼康D3300 单反相机专用 高透防刮屏幕保护膜/贴膜  
商品价格：18.90                              
                                            
商品ID：1119455
商品名称：麦富迪宠物零食 纯天然鸡胸肉卷牛皮狗咬胶200g*2袋  
商品价格：69.00                              
                                            
商品ID：1119456
商品名称：麦富迪 狗粮 金毛专用成犬粮10kg  
商品价格：
'''