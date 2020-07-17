# coding=utf-8
import requests,json,xlwt,ssl,sys,re
import brotli,datetime
import hashlib,base64
def getLbPhone():
    headers2 = {
        'authority':'www.lubanx.com',
        'method': 'GET',
        'path': '/cod/jinritemai/goodsRank?p=1&s=50&keyword=&sortRule=0&firstCategory=5&secondCategory=0&thirdCategory=0&storeType=1&onShelf=0',
        'scheme': 'https',
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'session=NmFkZWE4NzUtZTIwNS00ZjczLWE1MzAtZjY3ZjlmODAxOGVi; Hm_lvt_addf109ac734cd9bb1733b8328cc9c5d=1591884626,1591888360; Hm_lpvt_addf109ac734cd9bb1733b8328cc9c5d=1591889000; vue_admin_template_token=undefined; sidebarStatus=0',
        #'referer': 'https://www.lubanx.com/lubanx/',
        #'cache-control': 'no-cache',
        #'pragma': 'no-cache',
        #'sec-fetch-dest': 'empty',
       # 'sec-fetch-mode': 'cors',
        #'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.14 Safari/537.36'
    }
    k = 1
    pageSize=20
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'联系方式', cell_overwrite_ok=True)
    rowTitle = [u'店铺名称',u'商品标题',u'电话',u'商品链接']
    for i in range(0, len(rowTitle)):
        sheet1.write(0, i, rowTitle[i])
    for page in range(1,80):
        shop_url ='https://www.lubanx.com/cod/jinritemai/goodsRank?p='+str(page)+'&s=50&keyword=&sortRule=0&firstCategory=5&secondCategory=0&thirdCategory=0&storeType=1&onShelf=0'
        shop_response = requests.get(url=shop_url, headers=headers2, verify=False)
        shop_res = shop_response.json()
        print(shop_res)
        for shop_ki in shop_res['data']['list']:
            #try:
                goodsId = shop_ki['goodsId']
                goodsUrl = shop_ki['goodsUrl']
                moblie_url = 'https://ec.snssdk.com/product/lubanajaxstaticitem?id=' + str(
                    goodsId) + '&token=38bf3df39e0fbcb773cd2372e2d6dec7&page_id=' + str(goodsId) + '&b_type_new=0'
                #print(moblie_url)
                # print(moblie_url, item_id, redirect)
                moblie_response = requests.get(moblie_url)
                moblie_res = moblie_response.json()
                company_name = moblie_res['data']['company_name']
                name = moblie_res['data']['name']
                mobile = moblie_res['data']['mobile']
                if (mobile == '' or mobile == None or len(mobile)<8):
                    continue
                sheet1.write(k, 0, company_name)
                sheet1.write(k, 1, name)
                sheet1.write(k, 2, mobile)
                sheet1.write(k, 3, goodsUrl)
                k += 1

            #except Exception as es:
                #print(es)
                continue
        print(page)
        print("执行保存")
        f.save('D:/鲁班-服饰内衣'+datetime.datetime.now().strftime('%Y%m%d')+'.xls')




# MD5加密
def signmd5(page):
    list1 = [100, 97, 116, 95, 115, 111, 117, 114, 99, 101, 95, 116, 121, 112, 101, 37, 51, 68, 49, 37, 50, 54, 112, 97,
            103, 101, 37, 51, 68, 49, 37, 50, 54, 112, 97, 103, 101, 76, 105, 115, 116, 37, 51, 68, 50, 48, 37, 50, 54,
            107, 101, 121, 37, 51, 68, 55, 55, 99, 57, 56, 50, 98, 99, 99, 97, 53, 100, 98, 57, 49, 98, 98, 102, 48, 53,
            52, 51, 56, 56, 54, 99, 98, 52, 52, 48, 100, 51]
    list=[100,97,116,95,115,111,117,114,99,101,95,116,121,112,101,37,51,68,49,37,50,54,112,97,103,101,37,51,68,51,37,50,54,112,97,103,101,76,105,115,116,37,51,68,50,48,37,50,54,107,101,121,37,51,68,97,97,49,57,101,55,52,57,52,55,53,56,50,50,100,101,49,49,101,55,57,50,52,100,100,55,50,56,56,102,54,51]
    if page < 10:
        list[29] = 48 + page
    if page>9 and  page<100:
        list.insert(30,48 + int((page / 1) % 10))
        list[29] = 48 + int((page / 10) % 10)
    if page > 99 and page < 1000:
        list.insert(30, 48 + int((page / 10) % 10))
        list.insert(31, 48 + int((page / 1) % 10))
        list[29] = 48 + int((page / 100) % 10)
    if page > 999 and page < 10000:
        list.insert(30, 48 + int((page / 100) % 10))
        list.insert(31, 48 + int((page / 10) % 10))
        list.insert(32, 48 + int((page / 1) % 10))
        list[29] = 48 + int((page / 1000) % 10)
    strlist = str(list).replace('[', '').replace(']', '').replace(" ", "")
    res = hashlib.md5(strlist.encode()).hexdigest()
    return res








def getErLangChaPhone():
    k = 1
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'联系方式', cell_overwrite_ok=True)
    rowTitle = [u'公司名称',u'商品名称',u'电话',u'商品链接',u'产品最小单价',u'产品最大单价']
    for i in range(0, len(rowTitle)):
        sheet1.write(0, i, rowTitle[i])
    for ki in range(1, 10):
        try:
            url = 'https://www.erlangcha.com/api/list?page='+str(ki)+'&pageList=20&dat_source_type=1'
            sign = signmd5(ki)
            header = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                # 'Cookie': 'UM_distinctid=1732c1ce3dd241-0e60cc29f896ca-58133018-144000-1732c1ce3de6ad; CNZZDATA1277880260=765441170-1594167720-%7C1594167720',
                'Csrf-Sign': 'db3d3fe0cefc83c2ede6fd80ed0c9e0c',
                'Host': 'www.erlangcha.com',
                'Keep-At': '1594203116',
                'Keep-Csrf': 'cabbd66dd58ccf36c5e3119685ef39eb',
                'Keep-Mt': '8839',
                'Pragma': 'no-cache',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'sign': sign,
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.14 Safari/537.36'
            }
            pro_response=requests.get(url=url,headers=header)
            pro_res = pro_response.json()
            for pro_ki in pro_res['data']['content']:
                try:
                    redirect = pro_ki['shop_link']
                    item_id = redirect[52:72]
                    moblie_url = 'https://ec.snssdk.com/product/lubanajaxstaticitem?id=' + str(
                        item_id) + '&token=38bf3df39e0fbcb773cd2372e2d6dec7&page_id=' + str(item_id) + '&b_type_new=0'
                    print(moblie_url)
                    moblie_response = requests.get(moblie_url)
                    moblie_res = moblie_response.json()
                    company_name = moblie_res['data']['company_name']
                    name = moblie_res['data']['name']
                    mobile = moblie_res['data']['mobile']
                    sku_min_price = moblie_res['data']['sku_min_price']/100
                    sku_max_price = moblie_res['data']['sku_max_price']/100
                    if (mobile == '' or mobile == None):
                        continue
                    sheet1.write(k, 0, company_name)
                    sheet1.write(k, 1, name)
                    sheet1.write(k, 2, mobile)
                    sheet1.write(k, 3, redirect)
                    sheet1.write(k, 4, sku_min_price)
                    sheet1.write(k, 5, sku_max_price)
                    k += 1
                except Exception as es:
                    print("异常:" + es)
                    continue
        except Exception as e:
            print("系统异常:" + e)
            continue
        print("执行保存"+str(ki))
        f.save('D:/鲁班商品排行-13.xls')

def est():
    for i in range(1,15):
        url = 'https://www.erlangcha.com/api/list?page='+str(i)+'&pageList=20&dat_source_type=1'
        sign=signmd5(i)
        header = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                # 'Cookie': 'UM_distinctid=1732c1ce3dd241-0e60cc29f896ca-58133018-144000-1732c1ce3de6ad; CNZZDATA1277880260=765441170-1594167720-%7C1594167720',
                'Csrf-Sign': 'db3d3fe0cefc83c2ede6fd80ed0c9e0c',
                'Host': 'www.erlangcha.com',
                'Keep-At': '1594203116',
                'Keep-Csrf': 'cabbd66dd58ccf36c5e3119685ef39eb',
                'Keep-Mt': '8839',
                'Pragma': 'no-cache',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'sign': sign,
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.14 Safari/537.36'
            }
        pro_response = requests.get(url=url, headers=header)
        pro_res = pro_response.content
        print(pro_res)



getErLangChaPhone()
#est()








