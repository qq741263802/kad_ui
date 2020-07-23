# coding=utf-8
import requests,json,xlwt,ssl,sys,re
import brotli,datetime,time
import hashlib,base64,os
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
    #鲁班
    list2 = [100,97,116,95,115,111,117,114,99,101,95,116,121,112,101,37,51,68,49,37,50,54,112,97,103,101,37,51,68,50,37,50,54,107,101,121,37,51,68,56,51,100,48,101,99,55,99,48,52,51,52,51,97,50,56,53,99,97,100,54,50,49,102,97,48,100,100,99,97,101,97]
    # 抖音
    list1=[100,97,116,95,115,111,117,114,99,101,95,116,121,112,101,37,51,68,50,37,50,54,112,97,103,101,37,51,68,49,37,50,54,107,101,121,37,51,68,56,51,100,48,101,99,55,99,48,52,51,52,51,97,50,56,53,99,97,100,54,50,49,102,97,48,100,100,99,97,101,97]
    # 今日上新
    list=[100,97,116,95,115,111,117,114,99,101,95,116,121,112,101,37,51,68,49,37,50,54,112,97,103,101,37,51,68,49,37,50,54,107,101,121,37,51,68,56,51,100,48,101,99,55,99,48,52,51,52,51,97,50,56,53,99,97,100,54,50,49,102,97,48,100,100,99,97,101,97]
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
    rowTitle = [u'联系人ID',u'姓名',u'电话',u'公司',u'职位',u'地址','备注','邮箱','微信号','价格','销量','客服电话','负责人姓名','负责人电话','来源','类型','级别','状态','媒体','意向程度','运营续费','运营状态','开户数','负责人','共享给员工','共享给部门']
    for i in range(0, len(rowTitle)):
        sheet1.write(0, i, rowTitle[i])
    for ki in range(1, 2000):
        time.sleep(30)
        try:
            #url1='https://www.erlangcha
            # .com/api/getShopList?page='+str(ki)+'&dat_source_type=3'
            url = 'https://www.erlangcha.com/api/toadyNewProduct?dat_source_type=1&page='+str(ki)+''
            sign = signmd5(ki)
            print(sign)
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
            print(pro_res)
            if(pro_res['code']==400 or pro_res['code']==500 or pro_response.status_code!=200):
                continue
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
                    price=str(sku_min_price)+'-'+str(sku_max_price)
                    #sales_volume = pro_ki['sales_volume']
                    sales_volume=0
                    shopid = moblie_res['data']['shop_id']
                    shopmobileurl='https://luban.snssdk.com/shop/info?id=' + str(shopid) + '&_ts=1595258534707'
                    shopmobile_response = requests.get(shopmobileurl)
                    shopmobile_res = shopmobile_response.json()
                    shopmobil=shopmobile_res['data']['mobile']
                    if (mobile == '' or mobile == None or len(mobile) < 8):
                        continue
                    if (shopmobil == '' or shopmobil == None):
                        continue
                    sheet1.write(k, 3, company_name)
                    sheet1.write(k, 6, name)
                    sheet1.write(k, 2, mobile)
                    sheet1.write(k, 5, redirect)
                    sheet1.write(k, 9, price)
                    sheet1.write(k, 10, sales_volume)
                    sheet1.write(k, 11, shopmobil)
                    k += 1
                except Exception as es:
                    #print("异常:" + es)
                    continue
        except Exception as e:
            #print("系统异常:" + e)
            continue
        print("执行保存"+str(ki))
        f.save('D:/二郎查鲁班商品排行-'+str(os.getpid())+'.xls')





getErLangChaPhone()










