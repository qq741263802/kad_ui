# coding=utf-8
import requests,json,xlwt,ssl,sys,re
import brotli,datetime

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

def getErLangChaPhone():
    erlangchaheader1 = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'UM_distinctid=173298f7570e1-0560294cff42d7-c343162-100200-173298f7571cb; CNZZDATA1277880260=1891817800-1594125318-%7C1594130901',
        'Csrf-Sign': '5b3c748d7f9200a930de571c49bd5b74',
        'Host': 'www.erlangcha.com',
        'Keep-At': '1594136929',
        'Keep-Csrf': 'cabbd66dd58ccf36c5e3119685ef39eb',
        'Keep-Mt': '8811',
        'sign': '54289ee201bef0f85f5c23d8338bba41',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    erlangchaheader2={
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'UM_distinctid=1732c1ce3dd241-0e60cc29f896ca-58133018-144000-1732c1ce3de6ad; CNZZDATA1277880260=765441170-1594167720-%7C1594167720',
        'Csrf-Sign': '8414e61061650d7961990bd746ae5df2',
        'Host': 'www.erlangcha.com',
        'Keep-At': '1594173560',
        'Keep-Csrf': 'cabbd66dd58ccf36c5e3119685ef39eb',
        'Keep-Mt': '590',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'sign': '165f3ea2ac3975edd97ca292883951f1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.14 Safari/537.36'
    }
    k = 1
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'联系方式', cell_overwrite_ok=True)
    rowTitle = [u'公司名称',u'商品名称',u'电话',u'商品链接',u'产品最小单价',u'产品最大单价']
    for i in range(0, len(rowTitle)):
        sheet1.write(0, i, rowTitle[i])
    for ki in range(1, 99):
        try:
            url = 'https://www.erlangcha.com/api/toadyNewProduct?dat_source_type=1&page='+str(ki)+''
            pro_response=requests.get(url=url,headers=erlangchaheader2)
            pro_res = pro_response.json()
            print(pro_res)
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
                    print("异常" + es)
                    continue
        except Exception as e:
            print("异常" + e)
            continue
        print("执行保存"+str(ki))
        f.save('D:/鲁班今日上新榜.xls')



def est():
    header = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        #'Cookie': 'UM_distinctid=1732c1ce3dd241-0e60cc29f896ca-58133018-144000-1732c1ce3de6ad; CNZZDATA1277880260=765441170-1594167720-%7C1594167720',
        'Csrf-Sign': 'db3d3fe0cefc83c2ede6fd80ed0c9e0c',
        'Host': 'www.erlangcha.com',
        'Keep-At': '1594203116',
        'Keep-Csrf': 'cabbd66dd58ccf36c5e3119685ef39eb',
        'Keep-Mt': '8839',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'sign': '92a6f596a73a7bd1a97e7cb9979a1672',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.14 Safari/537.36'
    }
    url = 'https://www.erlangcha.com/api/toadyNewProduct?dat_source_type=1&page=26'
    pro_response = requests.get(url=url, headers=header)
    pro_res = pro_response.content
    print(pro_res)



#getErLangChaPhone()
est()