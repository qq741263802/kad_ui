# -*- coding: utf-8 -*-
import requests,json,xlwt,ssl,brotli



def createExcel():
    k = 1
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'测试数据', cell_overwrite_ok=True)
    rowTitle = [u'店名', u'shopid']
    for i in range(0, len(rowTitle)):
        sheet1.write(0, i, rowTitle[i])


def Gethtmlexcel():
        k=1
        f = xlwt.Workbook()
        sheet1 = f.add_sheet(u'测试数据', cell_overwrite_ok=True)
        rowTitle = [u'访问地址', u'价格', u'标题', u'推荐理由']
        for i in range(0, len(rowTitle)):
            sheet1.write(0, i, rowTitle[i])
        for i in range(80000, 80001):
            try:
                productId = 'https://www.kuaijinniu.com/m/goods?productId=' + str(i) + '&preview=1&layoutType=1&sid='
                url = 'https://www.kuaijinniu.com/rest/n/product/v2/detail?productId=' + str(
                    i) + '&from=1&orderRef=&callback='
                res = requests.get(url)
                if (res.status_code == 200):
                    respy = json.loads(res.text)
                    price = respy['data']['skuList'][0]['price'] / 100
                    productName = respy['data']['productName']
                    productDesc = respy['data']['productDesc']
                    sheet1.write(k, 0, productId)
                    sheet1.write(k, 1, price)
                    sheet1.write(k, 2, productName)
                    sheet1.write(k, 3, productDesc)
                    k += 1
                else:
                    print("获取异常,status_code：" + str(res.status_code))
            except Exception as e:
                 print("异常"+e)

                 continue
            f.save('D:/a.xls')



def getPhone():
    ssl._create_default_https_context = ssl._create_unverified_context
    shop_url='https://ds.appgrowing.cn/api/shop/rank?timeType=range&startDate=2020-06-05&endDate=2020-06-11&page=1&limit=20&sort=-quantitySoldIncr'
    #product_url='https://ds.appgrowing.cn/api/shop/product/rank?startDate=2020-05-12&endDate=2020-06-10&timeType=range&page=1&limit=20&sort=-quantitySoldIncr&isNew=false&matchType=product&shopId=ea4316bbe439555656e10718f3e1af73'
    headers2 = {
        'authority':'ds.appgrowing.cn',
        'method': 'GET',
        'path': '/api/leaflet/mt?startDate=2019-12-12&endDate=2020-06-08&order=-_score&isExact=false&keyword=%E8%A1%A3%E6%9C%8D&page=1&limit=60',
        'scheme': 'https',
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'GA1.2.1801623842.1591588262; NPS_Dialog-287498=gAAAAABeVISjTuGs3BvpNcZnvYK0uCs_XAnrmilhczWzvEG0_A1lGEg8OcVSP-W33R3amK0bTxCOFlZJH2ClU--kaPnwLVfxQw==; _gid=GA1.2.1024763389.1591848138; AG_Token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6ImU3ZDRjYTdiLWYzNjQtMzgxZS04N2YyLTU2MGVmNzYzMzYyMyIsImFjYyI6Mjg3NDk4LCJleHAiOjE1OTQ0NDAxNDgsImlhdCI6MTU5MTg0ODE0OX0.rgbSUZWcFHF3C1quieFrp6o2qqhHjG328I8VUW-b_TY; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22287498%22%2C%22%24device_id%22%3A%22172920d8f7b465-0ba3bc5efd71c3-58133018-1327104-172920d8f7c60c%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22https%3A%2F%2Fyoucloud.com%2Fservice%2Finfo%2F%3Fyoumi_aff%22%2C%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%22172920d8f7b465-0ba3bc5efd71c3-58133018-1327104-172920d8f7c60c%22%7D',
        'referer': 'https://ds.appgrowing.cn/leaflet?startDate=2019-12-12&endDate=2020-06-08&order=-_score&isExact=false&keyword=%E8%A1%A3%E6%9C%8D&page=1',
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.14 Safari/537.36',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'sec-fetch-dest': 'no-cache',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin'
    }
    headers = {
        'authority':'ds.appgrowing.cn',
        'method': 'GET',
        'path': '/api/leaflet/mt?startDate=2019-12-12&endDate=2020-06-08&order=-_score&isExact=false&keyword=%E7%9A%AE%E9%9E%8B&page=1&limit=60',
        'scheme': 'https',
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate',#, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'GA1.2.1801623842.1591588262; NPS_Dialog-287498=gAAAAABeVISjTuGs3BvpNcZnvYK0uCs_XAnrmilhczWzvEG0_A1lGEg8OcVSP-W33R3amK0bTxCOFlZJH2ClU--kaPnwLVfxQw==; _gid=GA1.2.1024763389.1591848138; AG_Token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6ImU3ZDRjYTdiLWYzNjQtMzgxZS04N2YyLTU2MGVmNzYzMzYyMyIsImFjYyI6Mjg3NDk4LCJleHAiOjE1OTQ0NDAxNDgsImlhdCI6MTU5MTg0ODE0OX0.rgbSUZWcFHF3C1quieFrp6o2qqhHjG328I8VUW-b_TY; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22287498%22%2C%22%24device_id%22%3A%22172920d8f7b465-0ba3bc5efd71c3-58133018-1327104-172920d8f7c60c%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22https%3A%2F%2Fyoucloud.com%2Fservice%2Finfo%2F%3Fyoumi_aff%22%2C%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%22172920d8f7b465-0ba3bc5efd71c3-58133018-1327104-172920d8f7c60c%22%7D',
        'referer': 'https://ds.appgrowing.cn/leaflet?startDate=2019-12-12&endDate=2020-06-08&order=-_score&isExact=false&keyword=%E7%9A%AE%E9%9E%8B&page=1',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'if-none-match':'W/"1de8f09fa55c512546152acc5565175b"'
    }
    k = 1
    pageSize=20
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'联系方式', cell_overwrite_ok=True)
    rowTitle = [u'店铺名称',u'商品标题',u'电话',u'商品链接']
    for i in range(0, len(rowTitle)):
        sheet1.write(0, i, rowTitle[i])
    shop_response = requests.get(url=shop_url,headers=headers2,verify=False)
    shop_res=shop_response.json()
    for shop_ki in shop_res['data']:
        try:
            shop_id = shop_ki['shopId']
            product_url = 'https://ds.appgrowing.cn/api/shop/product/rank?startDate=2020-05-13&endDate=2020-06-11&timeType=range&page=1&limit=20&sort=-quantitySoldIncr&isNew=false&matchType=product&shopId=' + str(shop_id) + ''
            print(product_url)
            item_response = requests.get(url=product_url, headers=headers2, verify=False)
            item_res = item_response.json()
            totalCount = item_res['total']
            if (totalCount % pageSize == 0):
                page = (int)(totalCount / pageSize)
            else:
                page = (int)(totalCount / pageSize + 1)
            for i in range(1, page + 1):
                pro_url = 'https://ds.appgrowing.cn/api/shop/product/rank?startDate=2020-05-13&endDate=2020-06-11&timeType=range&page=' + str(
                    i) + '&limit=20&sort=-quantitySoldIncr&isNew=false&matchType=product&shopId=' + str(shop_id) + ''
                print(pro_url)
                pro_response = requests.get(url=pro_url, headers=headers2, verify=False)
                pro_res = pro_response.json()
                for pro_ki in pro_res['data']:
                    try:
                        redirect = pro_ki['redirect']
                        item_id = redirect[52:72]
                        moblie_url = 'https://ec.snssdk.com/product/lubanajaxstaticitem?id=' + str(item_id) + '&token=38bf3df39e0fbcb773cd2372e2d6dec7&page_id=' + str(item_id) + '&b_type_new=0'
                        print(moblie_url)
                        #print(moblie_url, item_id, redirect)
                        moblie_response = requests.get(moblie_url)
                        moblie_res = moblie_response.json()
                        company_name = moblie_res['data']['company_name']
                        name = moblie_res['data']['name']
                        mobile = moblie_res['data']['mobile']
                        if(mobile=='' or mobile==None):
                            continue
                        sheet1.write(k, 0, company_name)
                        sheet1.write(k, 1, name)
                        sheet1.write(k, 2, mobile)
                        sheet1.write(k, 3, redirect)
                        k += 1
                    except Exception as es:
                        print("异常" + es)
                        continue
        except Exception as e:
            print("异常" + e)
            continue
        print("执行保存")
        f.save('D:/a.xls')


