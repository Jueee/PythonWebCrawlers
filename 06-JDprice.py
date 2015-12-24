'''
简单爬虫获取京东的商品价格
'''

'''
方法：通过京东移动商城（因为它没有把价格藏在js中）
'''
import urllib.request
import re
import xlwt

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
    m = re.search(r'<div class="prod-price">.*?<span>(.*?)</span>([^\s]*).*</div>',html,re.S)
    if m:
        jdprice = m.group(2)
    
    print('商品ID：%s' % jdid)
    print('商品名称：%s' % jdname)
    print('商品价格：%s' % jdprice)
    return {'jdid':jdid,'jdname':jdname,'jdprice':jdprice}

if __name__ != '__main__':
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


'''
将价格结果存入Excel
'''
# 生成a,b两个jdid之间的List
def get_jd_price_list(a, b):
    jd_list = []
    for x in range(a, b):
        jd_list.append(get_jd_price(x))
    return jd_list 

# 生成a,b两个jdid之间的Excel
def get_jd_price_excel(a,b):
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet 1')
    sheet.write(0,0,'number')
    sheet.write(0,1,'jdid')
    sheet.write(0,2,'jdname')
    sheet.write(0,3,'jdprice')
    jd_lists = get_jd_price_list(a,b)
    for x in range(len(jd_lists)):
        sheet.write(x+1, 0, x+1)
        sheet.write(x+1, 1, jd_lists[x].get('jdid'))
        sheet.write(x+1, 2, jd_lists[x].get('jdname'))
        sheet.write(x+1, 3, jd_lists[x].get('jdprice'))
    wbk.save('result//06-JDprice//jdprice'+str(a)+'-'+str(b)+'.xls')
    print('生成 Excel 成功！')


if __name__ == '__main__':
    get_jd_price_excel(1119452,1119500)
    