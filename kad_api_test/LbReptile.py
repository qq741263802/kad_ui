# coding=utf-8
import requests,json,xlwt,ssl,sys,re
import brotli,datetime
import hashlib,base64,time,os
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








