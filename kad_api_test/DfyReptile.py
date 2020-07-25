# coding=utf-8
import requests,json,xlwt,ssl,sys,re
import brotli,datetime
import hashlib,base64,time,os



def getDfyPhone():
    k = 1
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'联系方式', cell_overwrite_ok=True)
    rowTitle = [u'联系人ID',u'姓名',u'电话',u'公司',u'职位',u'地址','备注','邮箱','微信号','价格','销量','客服电话','负责人姓名','负责人电话','来源','类型','级别','状态','媒体','意向程度','运营续费','运营状态','开户数','负责人','共享给员工','共享给部门']
    for i in range(0, len(rowTitle)):
        sheet1.write(0, i, rowTitle[i])
    for ki in range(1, 1000):
        try:
            url = 'https://luban.api.duofangyun.com/landingPageList?page='+str(ki)+'&pagesize=20&sort=create_date'
            header = {
                'authority': 'luban.api.duofangyun.com',
                'method': 'POST',
                'path': '/landingPageList?page=1&pagesize=20&sort=create_date',
                'scheme': 'https',
                'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'zh-CN,zh;q=0.9',
                'cookie': 'session=NmFkZWE4NzUtZTIwNS00ZjczLWE1MzAtZjY3ZjlmODAxOGVi; Hm_lvt_addf109ac734cd9bb1733b8328cc9c5d=1591884626,1591888360; Hm_lpvt_addf109ac734cd9bb1733b8328cc9c5d=1591889000; vue_admin_template_token=undefined; sidebarStatus=0',
                'access-control-allow-credentials': 'true',
                'access-control-allow-origin': '*',
                'accesstoken': '27c3f940305803aeOuqDViAYCo+e4I5Wz3bHMV5tPDukt71HGYaXrTqtonFpFWkuZDYDmaXkLpERE/FEPTMd14xx2vrU46eALm5KggbgDQA/uIZ1j6OHwEhhNXHIjKMfHaGmozh9bpSmV26G1nJzpSH7zxikq5NgR9Zd8GTu3HvCtuS8ROr48vWAOAYOSzO3r91GpWHWhmisGg',
                'cache-control': 'no-cache',
                'content-length': '0',
                'origin': 'https://luban.duofangyun.com',
                'pragma': 'no-cache',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.14 Safari/537.36'
            }
            pro_response=requests.post(url=url,headers=header)
            pro_res = pro_response.json()
            print(pro_res)
            if(pro_response.status_code!=200):
                continue
            for pro_ki in pro_res['data']['data']:
                try:
                    redirect = pro_ki['source_url']
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
                    if(sku_min_price==sku_max_price):
                        price=sku_min_price
                    else:
                        price = str(sku_min_price) + '-' + str(sku_max_price)
                    sales_volume = pro_ki['sales_volume']
                    #sales_volume=0
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
        f.save('D:/多方云鲁班商品排行-'+str(os.getpid())+'.xls')



getDfyPhone()